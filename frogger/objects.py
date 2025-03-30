
import pygame
from maps import *
from observer import Observable
from time_manager import TimeManager

class Object(Observable):
    def __init__(self, type, x, y, movement):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.image_original = IMAGES[self.type]
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.movement = movement
    
    def update(self):
        self.rect.x += round(self.movement * TimeManager.get_delta_time(), 2)

        if self.rect.x < -OBJECT_WIDTH:
            self.rect.x = SCREEN_WIDTH + OBJECT_WIDTH
        elif self.rect.x > SCREEN_WIDTH + OBJECT_WIDTH:
            self.rect.x = -OBJECT_WIDTH