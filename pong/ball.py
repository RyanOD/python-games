import pygame
import random
import math

class Ball:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.radius = 10
        self.color = (255, 255, 255)
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.speed = 0
        self.speed_max = 15
        self.speed_x = 0
        self.speed_y = 0
        self.moving = False
        self.angle = 0
    
    def __repr__(self):
        return f"ball "

    def __str__(self):
        return f"ball.x = {self.x}\nball.y = {self.y}\nball.radius = {self.radius}\nball.color = {self.color}\nball.speed = {self.speed}"
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def move(self, screen):
        self.x += self.speed_x
        self.y += self.speed_y

    def serve(self):
        self.angle = math.radians(random.randint(0, 50))
        self.speed = random.randint(6, 10) * random.choice([-1, 1])
        self.speed_x = self.speed * math.cos(self.angle)
        self.speed_y = self.speed * math.sin(self.angle)
    
    def reset(self, screen):
        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.x = screen.width / 2
        self.y = screen.height / 2
    
    def collision_check(self, paddle_lt, paddle_rt):
        # if ball moving to the left and at same x coordinate as left paddle
        if self.speed_x < 0 and self.x - self.radius <= paddle_lt.rect.x + paddle_lt.rect.width:
            # check to see if vertical position of ball center is between top and bottom of paddle, indicating a collision
            if self.y >= paddle_lt.rect.y and self.y <= paddle_lt.rect.y + paddle_lt.rect.height:
                # reverse x-direction of ball
                if self.speed < self.speed_max:
                    self.speed_x *= -1.2
                self.speed_y += math.radians(random.randint(-80, 80))
                self.x = paddle_lt.x + paddle_lt.width + self.radius
        elif self.speed_x > 0 and self.x + self.radius >= paddle_rt.rect.x:
            if self.y >= paddle_rt.rect.y and self.y <= paddle_rt.rect.y + paddle_rt.rect.height:
                if self.speed < self.speed_max:
                    self.speed_x *= -1.2
                self.x = paddle_rt.rect.x - self.radius
                self.speed_y += math.radians(random.randint(-80, 80))
    
    def passed(self, screen):
        if self.x < -self.radius or self.x > screen.width + self.radius:
            self.reset(screen)