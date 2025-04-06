import pygame
from maps import *
from time_manager import TimeManager
from events import event_dispatcher

class Frog:
    def __init__(self):
        self.lives = 3
        self.death_timer = DEATH_TIMER
        self.width = FROG_WIDTH
        self.height = FROG_HEIGHT
        self.x = SCREEN_WIDTH // 2 - self.width
        self.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.carried_speed = 0
        self.alive = True

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
        self.movement_x = FROG_MOVEMENT_X
        self.movement_y = FROG_MOVEMENT_Y

    def carry(self, movement = 0):
        self.carried_speed = movement

    def update(self, direction='none'):
        if not self.on_screen():
            self.die()

        if not self.alive:
            if self.death_timer > 0:
                self.death_timer -= 1
            else:
                self.reset()

        if not self.in_water() or self.in_home():
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
    
    def on_screen(self):
        return 0 < self.rect.centerx < SCREEN_WIDTH and self.rect.y < SCREEN_HEIGHT
    
    def die(self):
        event_dispatcher.dispatch('play_sound', 'die_road')
        self.image = self.image_dead
        self.alive = False
        self.lives -= 1

        # screen boundary check / adjustment
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH - 14 # right side padding?
        elif self.rect.y > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - FROG_HEIGHT * 3

    def reset(self):
        self.image = self.image_original
        self.rect.x = SCREEN_WIDTH // 2 - self.width // 2
        self.rect.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.alive = True
        self.death_timer = DEATH_TIMER