import pygame
from maps import *

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.fill_road = BLACK
        self.fill_water = BLUE
        self.caption = self.set_caption(SCREEN_CAPTION)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.bg = self.get_bg(SCREEN_BG)

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_bg(self, bg_image):
        # Load the image
        bg_image = pygame.image.load(bg_image).convert()

        return bg_image