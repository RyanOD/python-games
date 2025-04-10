import pygame
from maps import *
from time_manager import TimeManager
from events import event_dispatcher

class Frog:
    def __init__(self, frog_data, start_x, start_y):
        self.lives = 3
        self.death_timer = 50
        self.width = frog_data.get_width()
        self.height = frog_data.get_height()
        self.x = start_x - self.width * 0.5
        self.y = start_y
        self.carried_speed = 0
        self.alive = True
        self.animated = False

        # load and scale frog sprite
        self.image_original = frog_data
        self.image = self.image_original
        #self.image_dead = frog_data['FD1']
        #self.image_home = frog_data['FH']

        # create rect for frog sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {
            "up": {"angle":0, "dx": 0, "dy": -1},
            "down": {"angle":180, "dx": 0, "dy": 1},
            "right": {"angle":-90, "dx": 1, "dy": 0},
            "left": {"angle":90, "dx": -1, "dy": 0},
        }

        # set frog x, y movement rates
        self.speed = 60

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
    
    def rotate_frog(self, degrees):
        self.image = pygame.transform.rotate(self.image_original, degrees)

    def handle_movement(self, direction):
            if direction in ("up", "down", "right", "left"):
                self.image = pygame.transform.rotate(self.image_original, self.orientations[direction]["angle"])
                self.rect.x += self.speed * self.orientations[direction]["dx"]
                self.rect.y += self.speed * self.orientations[direction]["dy"]

    def in_water(self):
        return 150 < self.rect.top < 480
    
    # the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
    def die(self):
        event_dispatcher.dispatch('play_sound', 'die_road')
        self.image = self.image_dead
        self.alive = False
        self.lives -= 1
    
    # reset the frog based on specified x, y screen positions
    def reset(self, start_x, start_y):
        self.image = self.image_original
        self.rect.x = start_x - self.width * 0.5
        self.rect.y = start_y
        self.alive = True
        self.death_timer = 50