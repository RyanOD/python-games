from events import event_dispatcher
from state_game import StateGame
import pygame

class StateClear(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()
        self.draw_flags = ['background', 'objects', 'frog', 'scoring', 'countdown', 'level', 'lives']

    def enter(self):
        self.timer = 600
        event_dispatcher.dispatch('play_sound', 'level_clear')

    def update(self, dt=None, events=None):
        if self.timer > 0:
            self.game.level.update(dt)
            self.timer -= dt * 100
        else:
            self.game.state_machine.change_state("welcome")

    def handle_input(self, dt=None, events=None):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.draw(self.bg_image, self.draw_flags)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

    def exit(self):
        self.game.level.num += 1
        self.game.frog.reset()
        self.game.countdown.reset()
        for home in self.game.homes:
            home['occupied'] = False
        self.game.level.objects.clear()
        self.game.level.load_level(self.game.level.num)
        event_dispatcher.dispatch('stop_sound', 'level_clear')