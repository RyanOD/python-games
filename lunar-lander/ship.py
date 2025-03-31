import pygame
from config import SHIP_IMAGE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_WIDTH
from time_manager import TimeManager


class Ship:
    def __init__(self):
        self.alive = True
        self.image = SHIP_IMAGE
        self.lives = 3
        self.x = SCREEN_WIDTH // 2 - SHIP_WIDTH // 2
        self.y = SCREEN_HEIGHT // 4
        self.velocity = 0
        self.acceleration = 0.5
        self.rotation = 10
        self.gravity = 2
    
    def update(self, movement):
        self.velocity += TimeManager.get_delta_time() / 1000 * self.gravity + self.acceleration
        self.y += self.velocity
        if self.lives > 0:
            self.handle_movement(movement)
    
    def handle_movement(self, movement):
        if movement == "accelerate":
            self.velocity += self.acceleration
        elif movement == "rotate_cw":
            pygame.transform.rotate(self.image, -self.rotation)
        elif movement == "rotate_ccw":
            pygame.transform.rotate(self.image, self.rotation)