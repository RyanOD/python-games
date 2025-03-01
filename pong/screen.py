import pygame

class Screen:
    def __init__(self, width, height, padding):
        self.width = width
        self.height = height
        self.padding = padding
        self.color = (255, 0, 0)
        self.surface = pygame.display.set_mode((self.width, self.height))

    def clear(self, color):
        self.surface.fill(color)
    
    def draw_line(self, color):
        pygame.draw.line(self.surface, color, (self.width / 2 -  1, 0), (self.width / 2 - 1, self.height), 2)
    
    def boundary_check(self, ball):
        # collision detection with top and bottom walls
        if ball.y + ball.radius + self.padding >= self.height or ball.y - ball.radius - self.padding <= 0:
            ball.speed_y *= -1