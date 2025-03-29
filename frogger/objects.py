
import pygame
from maps import *
from observer import Observable

class Object(Observable):
    def __init__(self, type, x, y, movement):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.pos_x = self.x
        self.pos_y = self.y
        self.image_original = IMAGES[self.type]
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.movement = movement
    
    def update(self, delta_time):
        self.pos_x += round(self.movement * delta_time, 2)

        if self.rect.x < -OBJECT_WIDTH:
            self.pos_x = SCREEN_WIDTH + OBJECT_WIDTH
        elif self.rect.x > SCREEN_WIDTH + OBJECT_WIDTH:
            self.pos_x = -OBJECT_WIDTH
        
        self.rect.x = int(self.pos_x)

        '''
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = -OBJECT_WIDTH'
        '''