import pygame
from maps import *

class Screen:
    def __init__(self, frog):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.caption = self.set_caption(SCREEN_CAPTION)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.bg = self.get_bg(SCREEN_BG)
        self.frog = frog
        self.homes = [
            {'frog': False, 'bounds': range(60, 120)},
            {'frog': False, 'bounds': (240, 300)},
            {'frog': False, 'bounds': (420, 480)},
            {'frog': False, 'bounds': (600, 660)},
            {'frog': False, 'bounds': (780, 840)}
            ]

    def update(self):
        if self.frog.rect.x < 600:
            for col, home in enumerate(self.homes):
                if self.frog.rect.centerx in home:
                    self.screen.surface.blit(self.frog.image_home, ((home[0] + home[1]) / 2, self.frog.rect.y))

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_bg(self, bg_image):
        # Load the image
        bg_image = pygame.image.load(bg_image).convert()

        return bg_image