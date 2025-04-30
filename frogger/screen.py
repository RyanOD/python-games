import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Screen:
    def __init__(self, game):
        self.game = game
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.lane_padding = 6
        self.lane_height = 50
        self.lane_width = 50
        self.surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Frogger Clone by Retro Clone")

    def draw(self, background=None, objects=None, frog=None, scoring=None, countdown=None):
        # clear screen
        self.surface.fill((0, 0, 0))

        # render background
        self.surface.blit(background, (0, 0))

        # render objects
        if objects:
            for object in objects:
                if object.image:
                    object.draw(object, self)

        # render frog
        if frog:
            frog.draw(self)

        # render timer
        if countdown:
            countdown.draw(self)

        # render scoring
        if scoring:
            self.game.scoring.draw(self)