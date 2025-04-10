import pygame
from observer import Observable
from time_manager import TimeManager

class Object(Observable):
    def __init__(self, type, images, x, y, movement):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.image = images[type]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.movement = movement
    
    def update(self):
        self.rect.x += round(self.movement * TimeManager.get_delta_time(), 2)
    
    def reset(self, screen):
        if self.rect.left > screen.width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = screen.width