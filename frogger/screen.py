import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Screen:
    def __init__(self, game):
        self.game = game
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.font_sm = pygame.font.Font("assets/upheavtt.ttf", 34)
        self.font_md_sm = pygame.font.Font("assets/upheavtt.ttf", 60)
        self.font_md = pygame.font.Font("assets/upheavtt.ttf", 100)
        self.font_lg = pygame.font.Font("assets/upheavtt.ttf", 200)

        # set screen window caption
        pygame.display.set_caption("Frogger Clone by Retro Clones")

    def draw(self, background=None, objects=None, frog=None, scoring=None, countdown=None, level=None, lives=None):
        # clear screen
        self.surface.fill((0, 0, 0))

        # render background
        self.surface.blit(background, (0, 0))

        # render objects
        if objects:
            for object in objects:
                if object.image:
                    object.draw(self)

        # render frog
        if frog:
            frog.draw(self)

        # render timer
        if countdown:
            countdown.draw(self)

        # render scoring
        if scoring:
            scoring.draw(self)

        # render level details
        if level:
            level.draw(self)

        # render frog lives icons
        if lives:
            lives.draw(self)