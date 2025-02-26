import pygame
import random
import math

class Ball:
    def __init__(self, radius, color, x, y):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.moving = False
        self.angle = 0
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def move(self, screen):
        self.x -= self.speed_x
        self.y += self.speed_y

        # collision detection with top and bottom walls
        if self.y + self.radius + screen.padding >= screen.height or self.y - self.radius - screen.padding <= 0:
            self.speed_y *= -1

    def serve(self):
        self.angle = math.radians(random.choice([30, 45, 60, 120, 135, 150]))
        self.speed = random.randint(2, 3)
        self.speed_x = self.speed * math.cos(self.angle)
        self.speed_y = self.speed * math.sin(self.angle)
    
    def reset(self, x, y):
        self.speed_x = 0
        self.speed_y = 0
        self.x = x
        self.y = y
    
    def collision_check(self, paddle):
        if(
            self.x - self.radius <= paddle.x + paddle.width and
            self.x + self.radius >= paddle.x and
            self.y >= paddle.y and
            self.y <= paddle.y + paddle.height
        ):
            self.speed_x *= -1
    
    def boundary_check(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if not self or self.x < -self.radius or self.x > SCREEN_WIDTH + self.radius:
            self.reset(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)