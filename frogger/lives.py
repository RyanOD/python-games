import pygame
from utils import get_image

class Lives():
    def __init__(self, num, images):
        self.num = num
        self.image = images["FL"]

    def increment(self):
        self.num += 1
    
    def decrement(self):
        self.num -= 1

    def draw(self, screen):
        for f in range(0, self.num):
            screen.surface.blit(self.image, (f * 30 + 5, 856))
