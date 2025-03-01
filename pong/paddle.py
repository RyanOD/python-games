import pygame

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 8
PADDLE_COLOR = (255, 255, 208)
PADDLE_SPEED = 8

class Paddle:
    def __init__(self, x, SCREEN_HEIGHT):
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.color = PADDLE_COLOR
        self.speed = PADDLE_SPEED
        self.x = x
        self.y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction, screen):
        if direction == "up" and self.rect.top > screen.padding:
            self.rect.y -= self.speed
        elif direction == "down" and self.rect.bottom < screen.height - screen.padding:
            self.rect.y += self.speed