
import pygame
from maps import *

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.fill_road = BLACK
        self.fill_water = BLUE
        self.caption = "Frogger Clone by Retro Clone"
        self.surface = pygame.display.set_mode((self.width, self.height))

    def reset(self):
        self.surface.fill(self.fill_water, (0, 0, self.width, 440))
        self.surface.fill(self.fill_road, (0, 440, self.width, self.height))
        pygame.display.set_caption(self.caption)