import pygame
from time_manager import TimeManager

class Frog:
    def __init__(self, images, start_x, start_y, play_sound):
        self.lives = 3
        self.width = images["F1"].get_width()
        self.height = images["F1"].get_height()
        self.carried_speed = 0
        self.alive = True
        self.play_sound = play_sound

        # load and scale frog sprites
        self.image_original = images["F3"]
        self.image = self.image_original
        self.menu_image = self.image_original
        self.image_moving = [images["F3"], images["F1"]]
        self.image_dying = [images["FD4"], images["FD3"], images["FD2"], images["FD1"]]
        self.image_home = images["FH"]

        # create rect for frog sprite (frog sprite location follows rect position)
        self.rect = self.image.get_rect()
        self.rect.x = start_x - self.width * 0.5
        self.rect.y = start_y
        
        # set up dying from image cycling timer data
        self.death_frame_duration = 40
        self.death_timer = self.death_frame_duration * len(self.image_dying)

        # frog sprite orientations options depending on player movement
        self.orientations = {
            "up": {"angle":0, "dx": 0, "dy": -1},
            "down": {"angle":180, "dx": 0, "dy": 1},
            "right": {"angle":-90, "dx": 1, "dy": 0},
            "left": {"angle":90, "dx": -1, "dy": 0},
        }

        # set frog pixel movement rate
        self.speed = 50

    # check if frog is in water zone and if so, set carry speed to zero then pass direction to move() method
    def update(self, direction='none'):
        if not self.in_water():
            self.carried_speed = 0
        self.move(direction)
    
    # if frog is alive, first manage carried movement then, if a direction has been passed, call handle_movement() method
    def move(self, direction):
        if self.alive:
            self.rect.x += round(self.carried_speed * TimeManager.get_delta_time(), 2)
            if direction:
                self.handle_movement(direction)

    # rotate frog and move in x or y direction then play hopping sound
    def handle_movement(self, direction):
            if direction in (self.orientations):
                self.image = pygame.transform.rotate(self.image_original, self.orientations[direction]["angle"])
                self.rect.x += self.speed * self.orientations[direction]["dx"]
                self.rect.y += self.speed * self.orientations[direction]["dy"]
                self.play_sound('hop')

    # check if frog is in water zone
    def in_water(self):
        return 150 < self.rect.top < 400
    
    # the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
    def die(self):
        self.carried_speed = 0
        self.play_sound('die')
        self.alive = False
        self.lives -= 1

    # reset the frog based on specified x, y screen positions
    def reset(self, start_x, start_y):
        self.image = self.image_original
        self.rect.x = start_x - self.width * 0.5
        self.rect.y = start_y
        self.alive = True
        self.death_timer = 160

    # when frog dies, begin death_timer countdown and rotate frog dying images based on time
    def dying_animation(self):
        if self.death_timer > 0:
            self.death_timer -= 1
            self.image = self.image_dying[min(len(self.image_dying) - 1, self.death_timer // self.death_frame_duration)]
            return False
        return True