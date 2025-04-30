import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Countdown:
    def __init__(self):
        self.countdown_width = 360
        self.countdown_tracker = 0

    def update(self, dt):
        self.countdown_tracker += dt 
        if self.countdown_tracker > 1:
            self.countdown_width -= 6
            self.countdown_tracker = 0

    def draw(self, screen):
        # draw countdown bar on screen
        pygame.draw.rect(screen.surface, (63, 232, 71), (SCREEN_WIDTH - self.countdown_width - 100, SCREEN_HEIGHT - 40, self.countdown_width, 30))