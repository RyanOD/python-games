import pygame
from maps import *
from time_manager import TimeManager
from events import event_dispatcher

class Frog:
    def __init__(self, screen):
        self.lives = 3
        self.death_timer = 50
        self.width = 20
        self.height = 20
        self.x = screen.width // 2 - self.width
        self.y = 15 * screen.lane_height + screen.lane_padding
        self.carried_speed = 0
        self.alive = True
        self.screen = screen

        # load and scale frog sprite
        self.image_original = IMAGES['F']
        self.image = self.image_original
        self.image_dead = IMAGES['FD']
        self.image_home = IMAGES['FH']

        # create rect for frog sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

        # set frog x, y movement rates
        self.movement_x = 60
        self.movement_y = 60

    def carry(self, movement = 0):
        self.carried_speed = movement

    def update(self, direction='none'):
        if not self.in_water():
            self.carry(0)

        self.move(direction)
    
    def move(self, direction):
        if self.alive:
            self.rect.x += round(self.carried_speed * TimeManager.get_delta_time(), 2)
            if direction:
                self.handle_movement(direction)
            
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
    
    def in_water(self):
        return 150 < self.rect.top < 480
    
    # the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
    def die(self):
        event_dispatcher.dispatch('play_sound', 'die_road')
        self.image = self.image_dead
        self.alive = False
        self.lives -= 1
    
    # reset the frog based on specified x, y screen positions
    def reset(self, x, y):
        self.image = self.image_original
        self.rect.x = x
        self.rect.y = y
        self.alive = True
        self.death_timer = 50