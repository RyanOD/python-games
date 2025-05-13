import pygame
from events import event_dispatcher
from frog_manager import *
from config import *

class Frog:
    def __init__(self, images):
        self.lives = 3
        self.carried_speed = 0
        self.alive = True

        # load and scale frog sprites
        self.image_original = images["F"]
        self.image = self.image_original
        self.image_lives = images["FL"]
        self.image_dying = [images["FD4"], images["FD3"], images["FD2"], images["FD1"]]
        self.image_home = images["FH"]

        # create rect for frog sprite (frog sprite location follows rect position)
        self.rect = self.image.get_rect()
        self.rect.x = FROG_START_X
        self.rect.y = FROG_START_Y
        
        # set up dying from image cycling timer data
        self.death_frame_duration = 40
        self.death_timer = self.death_frame_duration * len(self.image_dying)

        # frog sprite orientations options depending on player movement
        self.orientations = {
            "up": {"angle": 0, "dx": 0, "dy": -1},
            "down": {"angle": 180, "dx": 0, "dy": 1},
            "right": {"angle": -90, "dx": 1, "dy": 0},
            "left": {"angle": 90, "dx": -1, "dy": 0},
        }

        # set frog pixel movement rate
        self.speed = FROG_SPEED

    # check if frog is in water zone and if so, set carry speed to zero then pass direction to move() method
    def update(self):
        if not frog_in_water(self):
            self.carried_speed = 0
    
    def draw(self, screen):
        screen.surface.blit(self.image, (self.rect.x, self.rect.y))
        for f in range(0, self.lives):
            screen.surface.blit(self.image_lives, (f * 30 + 5, 856))

    # if frog is alive, first manage carried movement then, if a direction has been passed, call handle_movement() method
    def move(self, dt, direction='none'):
        if self.alive:
            self.rect.x += round(self.carried_speed * dt, 2)
            if direction:
                self.handle_movement(direction)

    # rotate frog and move in x or y direction then play hopping sound
    def handle_movement(self, direction):
            if direction in (self.orientations):
                self.image = pygame.transform.rotate(self.image_original, self.orientations[direction]["angle"])
                self.rect.x += self.speed * self.orientations[direction]["dx"]
                self.rect.y += self.speed * self.orientations[direction]["dy"]
                event_dispatcher.dispatch('play_sound', 'hop')
    
    def reset(self):
        self.alive = True
        self.lives = 3
        self.image = self.image_original
        self.rect.x = FROG_START_X
        self.rect.y = FROG_START_Y