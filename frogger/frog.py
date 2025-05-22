import pygame
from events import event_dispatcher
from config import *

class Frog:
    def __init__(self, lives, images):
        self.carried_speed = 0
        self.alive = True
        self.lives = lives

        # load and scale frog sprites
        self.image_original = images["F"]
        self.image = self.image_original
        self.image_dying = [images["FD4"], images["FD3"], images["FD2"], images["FD1"]]
        self.image_drowning = [images["FDR3"], images["FDR2"], images["FDR1"]]
        self.image_home = images["FH"]

        # create rect for frog sprite (frog sprite location follows rect position)
        self.rect = self.image.get_rect()
        self.rect.x = FROG_START_X
        self.rect.y = FROG_START_Y
        
        # set up dying from image cycling timer data
        self.death_frame_duration = 20
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
        if not self.in_water():
            self.carried_speed = 0
    
    def draw(self, screen):
        screen.surface.blit(self.image, (self.rect.x, self.rect.y))

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
        self.image = self.image_original
        self.rect.x = FROG_START_X
        self.rect.y = FROG_START_Y

    # check if frog y position is within home (goal) row
    def in_home_row(self):
        return self.rect.top < 150

    # check x position of frog as compared to that of frog homes and return Boolean
    def in_home_col(self):
        return (
            (self.rect.left >= 43 and self.rect.right <= 107) or
            (self.rect.left >= 193 and self.rect.right <= 257) or
            (self.rect.left >= 343 and self.rect.right <= 407) or
            (self.rect.left >= 493 and self.rect.right <= 557) or
            (self.rect.left >= 643 and self.rect.right <= 707)
        )

    # check if frog is in water zone and return Boolean
    def in_water(self):
        return WATER_TOP < self.rect.top < WATER_BOTTOM

    # check if frog is in on an object (log or turtle) and return True / False based on overlap
    def on_object(self, object):
        overlap = max(0, min(self.rect.right, object.rect.right) - max(self.rect.left, object.rect.left))
        return overlap >= self.rect.width / 2

    # should frog go off screen left or right, reset position to on screen and return True
    def hits_boundary(self, screen):
        if self.rect.bottom > screen.height - 50:
            self.rect.bottom = screen.height - 50
        else:
            if self.rect.left < 0:
                self.rect.left = 0
                return True
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
                return True

    # the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
    def dies(self):
        self.carried_speed = 0
        if self.in_water():
            event_dispatcher.dispatch('play_sound', 'drown')
        else:
            event_dispatcher.dispatch('play_sound', 'die')
        self.alive = False
        self.lives.decrement()

    # when frog dies, begin death_timer countdown and cylce through frog dying images based on time and return Boolean
    def dying_animation(self):
        if self.death_timer > 0:
            self.death_timer -= 1
            if self.in_water():
                self.image = self.image_drowning[min(len(self.image_drowning) - 1, self.death_timer // self.death_frame_duration)]
            else:
                self.image = self.image_dying[min(len(self.image_dying) - 1, self.death_timer // self.death_frame_duration)]
            return False
        return True

    # reset the frog to game start position and image. Reset death timer.
    def reset(self):
        self.image = self.image_original
        self.rect.x = FROG_START_X
        self.rect.y = FROG_START_Y
        self.alive = True
        self.death_timer = self.death_frame_duration * len(self.image_dying)