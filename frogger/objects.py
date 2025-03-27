
import pygame
from maps import *

class Object:
    def __init__(self, type, x, y, speed, direction):
        self.type = type
        self.x = x
        self.y = y
        self.image_original = pygame.image.load(OBJECT_MAP[self.type]['image'])
        self.image = pygame.transform.scale(self.image_original, (OBJECT_HEIGHT, OBJECT_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed
        self.direction = direction
    
    def update(self, delta_time):
        if self.direction == 'left':
            self.rect.x -= self.speed * delta_time
        else:
            self.rect.x += self.speed * delta_time

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0