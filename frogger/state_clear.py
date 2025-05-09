from events import event_dispatcher
from state_game import StateGame
import pygame

class StateClear(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()

    def enter(self):
        self.timer = 400
        event_dispatcher.dispatch('play_sound', 'level_clear')

    def update(self, dt = None, events = None):
        if self.timer > 0:
            self.game.level.update(dt)
            self.timer -= 1
        else:
            self.game.frog.lives = -dt * 100

    def handle_input(self, dt = None, events = None):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.draw(self.bg_image, self.game.level.objects, self.game.frog, self.game.scoring, self.game.countdown)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

    def exit(self):
        self.time = 300