import pygame
from classes import *
from maps import *
from asset_paths import *

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.current_level = None
        self.level = Level(1)
        self.running = True
        self.playing = True
        self.hedge = pygame.transform.scale(pygame.image.load('assets/hedge.png'), (60, 60))
        self.lives = 3
        self.screen = Screen()
        self.surface = self.screen.surface
        self.frog = Frog(self.screen)
        self.input_handler = InputHandler(self.frog)
        self.collision_handler = CollisionHandler()

    def update(self):
        self.collision_handler.check_collisions(self.frog, self.level.objects)

    def draw(self):
        self.screen.clear()
        pygame.display.set_caption("Frogger Clone")
        if self.hedge:
            for i in range(0, self.screen.width, 60):
                self.screen.surface.blit(self.hedge, (i, 410))
                self.screen.surface.blit(self.hedge, (i, 890))

        for object in self.level.objects:
            self.screen.surface.blit(object.image, (object.x, object.y))

        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.x, self.frog.y))

        self.draw_grid()

        pygame.display.set_caption(self.screen.title)
        pygame.display.flip()

    def draw_grid(self):
        for i in range(0, self.screen.height, 80):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (0, i), (self.screen.width, i))

        for i in range(0, self.screen.width, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (i, 0), (i, self.screen.height))

    def game_over(self):
        return self.lives <= 0
