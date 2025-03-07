import pygame
from classes import *

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = True
        self.frog = Frog()
        self.lives = 3

    
    def update(self):
        pass

    def draw(self):
        pass

    def game_over(self):
        return self.lives <= 0
