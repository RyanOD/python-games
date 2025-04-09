
import pygame
from maps import *
from observer import Observable
from time_manager import TimeManager

class Object(Observable):
    def __init__(self, type, x, y, height, width, movement):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_original = IMAGES[self.type]
        self.image = self.image_original
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