
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
        self.bg = self.get_bg()

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))
        #pygame.display.set_caption(self.caption)

    def get_bg(self):
        # Load the image
        bg_image = pygame.image.load("assets/bg.png")

        # Convert the image for faster blitting (optional)
        bg_image = bg_image.convert()

        return bg_image