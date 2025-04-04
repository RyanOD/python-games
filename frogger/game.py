import pygame
from asset_paths import *
from frog import Frog
from level import Level
from input import InputHandler
from screen import Screen
from maps import *
from sound import SoundHandler
from collision import CollisionHandler
from time_manager import TimeManager

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.level: Level = Level(1)
        self.running: bool = 5
        self.playing: bool = True
        self.lives: int = 3
        self.screen = Screen()
        self.surface = self.screen.surface
        self.frog = Frog(self.screen)
        self.input_handler = InputHandler(self.frog)
        self.sound_handler = SoundHandler()
        self.collision_handler = CollisionHandler()
        self.sound_handler = SoundHandler()
    
    def update(self):
        if not self.frog.alive:
            self.frog.death_timer -= 1
        if self.frog.rect.y:
            self.collision_handler.check_collisions(self.frog, self.level.objects)
        for object in self.level.objects:
            object.update()
        self.frog.update()

    def draw(self):
        self.screen.reset()

        for object in self.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
                #pygame.draw.rect(self.screen.surface, (255, 255, 255), object.rect, 2)
                    
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))
            #pygame.draw.rect(self.screen.surface, (255, 0, 0), self.frog.rect, 2)

        #self.draw_grid()

        pygame.display.flip()

    def draw_grid(self):
        for i in range(0, self.screen.height, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (0, i), (self.screen.width, i))

        for i in range(0, self.screen.width, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (i, 0), (i, self.screen.height))

    def game_over(self):
        return self.lives <= 0