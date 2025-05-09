import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Countdown:
    def __init__(self):
        self.total = 360
        self.width = self.total
        self.tracker = 0

    def update(self, dt):
        self.tracker += dt 
        if self.tracker > 1:
            self.width -= 0.1 // dt
            self.tracker = 0

    def draw(self, screen):
        pygame.draw.rect(screen.surface, (63, 232, 71), (SCREEN_WIDTH - self.width - 100, SCREEN_HEIGHT - 40, self.width, 30))
    
    def reset(self):
        self.total = 360