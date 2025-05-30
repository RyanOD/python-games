import pygame
from state_game import StateGame
from events import event_dispatcher
from debug import draw_grid

class StatePlay(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()
        self.draw_flags = ['background', 'objects', 'frog', 'scoring', 'countdown', 'level', 'lives']

        # state specific attributes beyond background
        self.level_cleared = False

    def enter(self):
        event_dispatcher.dispatch('play_sound', 'main_theme')

    def update(self, dt=None, events=None):
        # delegate frog/object collision management to CollisionHandler class
        if self.game.frog.alive and not self.game.collision_handler.safe_collision(self.game.frog, self.game.level.objects):
            self.game.frog.dies()

        # delegate frog passive management to Frog class
        self.game.level.update(dt)

        # delegate frog passive management to Frog class
        self.game.frog.update()

        # delegate frog active movement to Frog class 
        self.game.frog.move(dt)

        # delegate scoring display management to Scoring class
        self.game.scoring.update()

        # update frog life status based on screen boundary collision (managed here because it involves Frog and Screen classes)
        if self.game.frog.hits_boundary(self.game.screen):
            self.game.frog.dies()
        
        if self.game.countdown.is_expired():
            self.game.frog.dies()
            self.game.countdown.reset()

        # check to see if frog makes it to home goal location
        home_col = self.game.frog.rect.centerx // 150

        if self.game.frog.in_home_row() and self.game.frog.alive:
            if not self.game.homes[home_col]['occupied']:
                event_dispatcher.dispatch('play_sound', 'landing_safe')
                self.game.homes[home_col]['occupied'] = True
                self.game.level.reset_rows()
                self.game.reset_level()
                self.game.frog.reset()
            else:
                self.game.frog.rect.top = 150 # prevent Frog from moving into occupied home slot
                self.game.frog.dies()

        if not self.game.frog.alive and self.game.frog.dying_animation():
            self.game.level.reset_rows()
            self.game.frog.reset()

        if all(home['occupied'] for home in self.game.homes):
            self.game.state_machine.change_state("clear")

        if self.game.lives.num == 0:
            self.game.state_machine.change_state("game_over")

        self.game.countdown.update(dt)

    def handle_input(self, dt=None, events=None):
        for event in events:
            if self.game.frog.alive:
                self.game.input_handler.handle_event(event, self.game, dt)

    def draw(self):
        # draw game assets
        self.game.screen.draw(self.bg_image, self.draw_flags)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

        #draw_grid(self.game.screen)

    def exit(self):
        event_dispatcher.dispatch('stop_sound', 'main_theme')

    # end game if all frog lives lost
    def game_over(self):
        return self.game.lives.num == 0