import pygame
from input_handler import *


class Game():
    def __init__(self):
        pygame.init()
        self.running = False
        self.playing = False
        #self.centerline_color = (255, 255, 255)
        #self.display = pygame.Surface((self.screen_width, self.screen_height))
        #self.surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        #self.surface.fill(self.screen_color)
        #self.key_up = False
        #self.key_down = False
        #pygame.display.set_caption("Pong Clone")
        clock = pygame.time.Clock()
    
    def GameLoop(self):
        while self.playing:
            self.input()
            self.update()
            self.draw()