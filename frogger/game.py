import pygame
from classes import *

class Game:
    def __init__(self, screen):
        pygame.init()
        self.running = True
        self.playing = True
        self.frog = Frog(screen)
        self.lives = 3
        self.input_handler = InputHandler(self.frog)
        self.screen = screen
    
    def update(self):
        pass

    def draw(self):
        self.screen.clear()
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.x, self.frog.y))
        pygame.display.set_caption(self.screen.title)
        pygame.display.flip()

    def game_over(self):
        return self.lives <= 0
