import pygame

class Ball:
    def __init__(self, radius, color, x, y):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)