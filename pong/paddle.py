import pygame

class Paddle:
    def __init__(self, x, y):
        self.height = 100
        self.width = 8
        self.color = (255, 255, 208)
        self.speed = 10
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y / 2, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction, screen):
        if direction == "up" and self.rect.top > screen.padding:
            self.rect.y -= self.speed
        elif direction == "down" and self.rect.bottom < screen.height - screen.padding:
            self.rect.y += self.speed
    
    def ai(self, ball):
        if ball.speed_x > 0:
            target = ball.y - self.height // 2
            if abs(target - self.rect.y) > 6:
                direction = 1 if target > self.rect.y else -1
                self.rect.y += self.speed * direction