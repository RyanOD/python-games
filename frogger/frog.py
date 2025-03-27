import pygame
from maps import *

class Frog:
    def __init__(self, screen):
        self.alive = True
        self.width = OBJECT_WIDTH
        self.height = OBJECT_HEIGHT
        self.x = screen.width // 2 - self.width // 2
        self.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.speed = 10

        # load and scale frog image
        self.image_original = pygame.transform.scale(pygame.image.load('assets/frog_1.png'), (self.width, self.height))
        self.image = self.image_original
        self.image_dead = pygame.transform.scale(pygame.image.load('assets/dead_4.png'), (self.width, self.height))

        # create a rect for frog image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + OBJECT_WIDTH // 2, self.y + OBJECT_HEIGHT // 2)
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

        # set frog x and y movement rates
        self.movement_x = 60
        self.movement_y = 60

    def update(self, direction):
        if self.alive:
            if direction == "up":
                self.image = pygame.transform.rotate(self.image_original, 0)
                self.rect.y -= self.movement_y
            elif direction == "down":
                self.image = pygame.transform.rotate(self.image_original, 180)
                self.rect.y += self.movement_y
            elif direction == "left":
                self.image = pygame.transform.rotate(self.image_original, 90)
                self.rect.x -= self.movement_x
            elif direction == "right":
                self.image = pygame.transform.rotate(self.image_original, -90)
                self.rect.x += self.movement_x