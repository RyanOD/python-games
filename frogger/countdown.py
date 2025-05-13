import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Countdown:
    def __init__(self):
        self.initial_width = 60
        self.pixels_per_second = 6
        self.width = self.initial_width
        self.tracker = 0

    def update(self, dt):
        self.tracker += dt 
        if self.tracker > 1:
            self.width -= self.pixels_per_second
            self.tracker = 0
        if self.width < 0:
            self.width = 0

    def draw(self, screen):
        pygame.draw.rect(screen.surface, (63, 232, 71), (SCREEN_WIDTH - self.width - 100, SCREEN_HEIGHT - 40, self.width, 30))
    
    def reset(self):
        self.width = self.initial_width
        self.tracker = 0

    def is_expired(self):
        return self.width <= 0