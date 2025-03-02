import pygame

class Paddle:
    def __init__(self, x_position, y_position):
        self.height = 100
        self.width = 8
        self.color = (255, 255, 208)
        self.speed = 8
        self.x_position = x_position
        self.y_position = y_position
        self.rect = pygame.Rect(self.x_position, self.y_position / 2, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction, screen):
        if direction == "up" and self.rect.top > screen.padding:
            self.rect.y -= self.speed
        elif direction == "down" and self.rect.bottom < screen.height - screen.padding:
            self.rect.y += self.speed