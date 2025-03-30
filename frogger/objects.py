
import pygame
from maps import *
from observer import Observable

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
    
    def update(self, delta_time):
        self.x += round(self.movement * delta_time, 2)

        if self.x < -OBJECT_WIDTH:
            self.x = SCREEN_WIDTH + OBJECT_WIDTH
        elif self.x > SCREEN_WIDTH + OBJECT_WIDTH:
            self.x = -OBJECT_WIDTH
        
        self.rect.x = int(self.x)

        '''
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = -OBJECT_WIDTH'
        '''