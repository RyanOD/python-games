import pygame
from classes import *

class Game:
    def __init__(self, screen):
        pygame.init()
        self.running = True
        self.playing = True
        self.frog = Frog(screen)
        self.hedge_road = pygame.transform.scale(pygame.image.load('assets/hedge_road.png'), (80, 80))
        self.hedge_water = pygame.transform.scale(pygame.image.load('assets/hedge_water.png'), (80, 80))
        self.lives = 3
        self.input_handler = InputHandler(self.frog)
        self.screen = screen
    
    def update(self):
        pass

    def draw(self):
        self.screen.clear()
        if self.hedge_water and self.hedge_road:
            for i in range(0, 900, 80):
                self.screen.surface.blit(self.hedge_water, (i, 400))
                self.screen.surface.blit(self.hedge_road, (i, 860))
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.x, self.frog.y))
        pygame.display.set_caption(self.screen.title)
        pygame.display.flip()

    def game_over(self):
        return self.lives <= 0
