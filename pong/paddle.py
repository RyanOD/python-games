import pygame

PADDLE_HEIGHT = 40
PADDLE_WIDTH = 8
PADDLE_COLOR = (255, 255, 208)
PADDLE_SPEED = 4

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.color = PADDLE_COLOR
        self.speed = PADDLE_SPEED

    def draw(self, screen):
        paddle = pygame.Rect(self.x, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, (255, 255, 208), paddle)

    def move(self, direction):
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed