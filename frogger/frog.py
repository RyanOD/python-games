import pygame
from maps import *
from time_manager import TimeManager

class Frog:
    def __init__(self, screen):
        self.screen = screen
        self.lives = 3
        self.death_timer = 250
        self.width = OBJECT_WIDTH
        self.height = OBJECT_HEIGHT
        self.x = self.screen.width // 2 - self.width // 2
        self.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.speed = 10
        self.carried_speed = 0
        self.alive = True

        # load and scale frog image
        self.image_original = IMAGES['F']
        self.image = self.image_original
        self.image_dead = IMAGES['FD']

        # create a rect for frog image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

        # set frog x and y movement rates
        self.movement_x = 60
        self.movement_y = 60

    def update(self, direction='none'):
        if self.alive:
            self.rect.x += round(self.carried_speed * TimeManager.get_delta_time(), 2)
            if direction:
                self.handle_movement(direction)
        else:
            self.lives -= 1
            self.image = self.image_dead
            self.death_timer -= 1
            if self.death_timer <= 0:
                self.reset()
    
    def carry(self, movement = 0):
        self.carried_speed = movement
            
    def handle_movement(self, direction):
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
    
    def reset(self):
        self.image = self.image_original
        self.rect.x = self.screen.width // 2 - self.width // 2
        self.rect.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.alive = True
        self.death_timer = 250