import pygame
from ship import Ship
from screen import Screen
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_HEIGHT, SHIP_WIDTH

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.lives = 3
        self.ship = Ship()
        self.screen = Screen()

    def update(self):
        pass

    def draw(self):
        self.screen.surface.blit(self.ship.image, (SCREEN_WIDTH // 2 - SHIP_WIDTH // 2, SCREEN_HEIGHT // 4))
        pygame.display.flip()

    def game_over(self):
        return self.lives <= 0