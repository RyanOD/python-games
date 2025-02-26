import pygame

class Screen:
    def __init__(self, width, height, padding):
        self.width = width
        self.height = height
        self.padding = padding
        self.surface = pygame.display.set_mode((self.width, self.height))

    def clear(self, color):
        self.surface.fill(color)
    
    def draw_line(self, color):
        pygame.draw.line(self.surface, color, (self.width / 2 -  1, 0), (self.width / 2 - 1, self.height), 2)