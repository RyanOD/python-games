import pygame
import random

from config import *

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.stars = self.create_stars()
        self.caption = self.set_caption(SCREEN_CAPTION)
        self.surface = pygame.display.set_mode((self.width, self.height))

        pygame.key.set_repeat(50, 50)

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        pass

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def create_stars(self):
        stars_data = []
        for _ in range(60):
            x = random.randint(SCREEN_PADDING, SCREEN_WIDTH - SCREEN_PADDING)
            y = random.randint(SCREEN_PADDING, SCREEN_HEIGHT - SCREEN_PADDING)
            color = random.choice([WHITE, WHITE1, WHITE2, RED])
            radius = random.randint(1, 3)
            stars_data.append({'color': color, 'position': (x, y), 'radius': radius})
        return stars_data

    def draw(self):
        self.surface.fill(BLACK)
        for star in self.stars:
            print(star)
            pygame.draw.circle(self.surface, star['color'], star['position'], star['radius'])