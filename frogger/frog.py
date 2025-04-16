import pygame
from time_manager import TimeManager

class Frog:
    def __init__(self, images, start_x, start_y, play_sound):
        self.lives = 3
        self.death_timer = 50
        self.width = images["F1"].get_width()
        self.height = images["F1"].get_height()
        self.carried_speed = 0
        self.alive = True
        self.play_sound = play_sound

        # load and scale frog sprites
        self.image_original = images["F1"]
        self.image = self.image_original
        self.menu_image = self.image_original
        self.image_dead = images["FD1"]
        self.image_home = images["FH"]

        # create rect for frog sprite
        self.rect = self.image.get_rect()
        self.rect.x = start_x - self.width * 0.5
        self.rect.y = start_y
        
        # set and track frog sprite orientation
        self.orientations = {
            "up": {"angle":0, "dx": 0, "dy": -1},
            "down": {"angle":180, "dx": 0, "dy": 1},
            "right": {"angle":-90, "dx": 1, "dy": 0},
            "left": {"angle":90, "dx": -1, "dy": 0},
        }

        # set frog x, y movement rates
        self.speed = 50

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
            if direction in (self.orientations):
                self.image = pygame.transform.rotate(self.image_original, self.orientations[direction]["angle"])
                self.rect.x += self.speed * self.orientations[direction]["dx"]
                self.rect.y += self.speed * self.orientations[direction]["dy"]
                self.play_sound('hop')

    def in_water(self):
        return 150 < self.rect.top < 400
    
    # the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
    def die(self):
        self.carry(0)
        self.play_sound('die')
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