import pygame
from observer import Observable
from time_manager import TimeManager

class Object(Observable):
    def __init__(self, type, images, x, y, movement):
        super().__init__()
        self.type = type
        self.image = images[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movement = movement
    
    # move object
    def update(self, dt):
        self.rect.x += round(self.movement * dt, 2)
    
    def reset(self, screen):
        if self.rect.left > screen.width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = screen.width