import pygame

def draw_grid(screen):
    for i in range(0, screen.height, 50):
        pygame.draw.line(screen.surface, (255, 255, 255), (0, i), (screen.width, i))

    for i in range(0, screen.width, 50):
        pygame.draw.line(screen.surface, (255, 255, 255), (i, 0), (i, screen.height))