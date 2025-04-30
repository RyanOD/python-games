import pygame
from state_game import StateGame
from state_clear import StateClear
from events import event_dispatcher
from frog_manager import *
from utils import get_bg_image
from debug import draw_grid

class StatePlay(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.level_cleared = False
        self.bg_image = pygame.image.load("assets/bg.png").convert()

        event_dispatcher.dispatch('play_sound', 'main_theme')

    def enter(self):
        pass

    def update(self, dt, events):
        # delegate frog/object collision management to CollisionHandler class
        if self.game.frog.alive and not self.game.collision_handler.safe_collision(self.game.frog, self.game.level.objects):
            frog_dies(self.game.frog)

        # delegate frog passive management to Frog class
        self.game.level.update(dt)

        # delegate frog passive management to Frog class
        self.game.frog.update()

        # delegate frog active movement to Frog class 
        self.game.frog.move(dt)

        # update frog life status based on screen boundary collision
        if self.game.frog.alive and not frog_on_screen(self.game.frog, self.game.screen):
            frog_dies(self.game.frog)

        # delegate scoring display management to Scoring class
        self.game.scoring.update(dt)
        
        # check to see if frog makes it to home goal location
        if frog_in_home_row:
            self.home_check()

        if not self.game.frog.alive and frog_dying_animation(self.game.frog):
            self.reset_level()

        if all(home['occupied'] for home in self.game.homes):
            self.game.state_machine.change_state(StateClear(self.game, dt))

        self.game.countdown.update(dt)

    def draw(self):
        # clear the screen
        self.game.screen.draw(self.bg_image, self.game.level.objects, self.game.frog, self.game.scoring, self.game.countdown)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, ((((150 * col + 50) + (150 * col + 100)) // 2 - self.game.frog.image_home.get_width() // 2), 104))

        #draw_grid(self.game.screen)

    def exit(self):
        event_dispatcher.dispatch('stop_sound', 'main_theme')

    # check if frog rect is in the goal home row and if so, update home occupied state to True, play sound effect and reset level
    def home_check(self):
        for col, home in enumerate(self.game.homes):
            if self.game.frog.rect.centerx in range(col * 150 + 50, col * 150 + 100) and frog_in_home_row(self.game):
                event_dispatcher.dispatch('play_sound', 'landing_safe')
                home['occupied'] = True
                self.reset_level()

    # reset visited state of all rows to False then reset frog
    def reset_level(self):
        self.game.scoring.reset()
        frog_reset(self.game.frog)
        #self.game.frog.reset()
    
    # end game if all frog lives lost
    def game_over(self):
        return self.game.lives == 0