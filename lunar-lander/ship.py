import pygame
from config import SHIP_IMAGE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_WIDTH, SHIP_HEIGHT
from time_manager import TimeManager


class Ship:
    def __init__(self):
        self.alive = True
        self.image_original = SHIP_IMAGE.convert_alpha()
        self.rotated_image = self.image_original
        self.rotated_rect = self.rotated_image.get_rect()
        self.lives = 3
        self.x = SCREEN_WIDTH // 2 - SHIP_WIDTH // 2
        self.y = SCREEN_HEIGHT // 4
        self.rect = pygame.Rect(self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT)
        self.pivot_x = self.x + SHIP_WIDTH // 2
        self.pivot_y = self.y + SHIP_WIDTH // 2
        self.velocity = 0
        self.acceleration = 0.5
        self.rotation = 0
        self.gravity = 2
        self.angle = 0
        self.v_rotation = 10
    
    def update(self, movement):
        self.velocity += TimeManager.get_delta_time() / 1000 * self.gravity + self.acceleration
        self.y += self.velocity
        if self.lives > 0:
            self.handle_movement(movement)
    
    def handle_movement(self, movement):
        if movement == "accelerate":
            self.velocity += self.acceleration
        elif movement == "rotate_cw":
            self.angle -= self.v_rotation
            self.rotated_image = self.image = pygame.transform.rotate(self.image_original, self.angle)
        elif movement == "rotate_ccw":
            self.angle += self.v_rotation
            self.rotated_image = self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.rotated_rect = self.rotated_image.get_rect()
        self.rotated_rect.center = self.image_original.get_rect().center