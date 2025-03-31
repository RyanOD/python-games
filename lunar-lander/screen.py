import pygame
import random

from config import *

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.bg = BLACK
        self.star = WHITE
        self.caption = self.set_caption(SCREEN_CAPTION)
        self.surface = pygame.display.set_mode((self.width, self.height))

        for _ in range(60):
            # Generate random position and size
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            radius = random.randint(1, 2)
        
            pygame.draw.circle(self.surface, random.choice([WHITE, WHITE1, WHITE2, RED]), (x, y), radius)
        
        pygame.display.flip()

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))
        for i in range(0, 50):
            pygame.draw.circle(self.surface, random.choice([WHITE, WHITE1, WHITE2]), (i, i * 3), 5)

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_bg(self, bg_image):
        # Load the image
        bg_image = pygame.image.load(bg_image).convert()

        return bg_image