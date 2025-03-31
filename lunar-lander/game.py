import pygame
from ship import Ship
from screen import Screen
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_HEIGHT, SHIP_WIDTH
from input import InputHandler

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.lives = 3
        self.ship = Ship()
        self.screen = Screen()
        self.input_handler = InputHandler(self.ship)

    def update(self):
        pass

    def draw(self):
        self.screen.draw()
        self.screen.surface.blit(self.ship.image, (self.ship.x, self.ship.y))
        pygame.display.flip()

    def game_over(self):
        return self.lives <= 0