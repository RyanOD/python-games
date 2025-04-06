import pygame
from asset_paths import *
from frog import Frog
from level import Level
from input import InputHandler
from screen import Screen
from home import Home
from maps import *
from sound import SoundHandler
from collision import CollisionHandler
from time_manager import TimeManager

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.level = Level(1)
        self.lives = 3
        self.frog = Frog()
        self.screen = Screen(self.frog)
        self.surface = self.screen.surface
        self.input_handler = InputHandler(self.frog)
        self.sound_handler = SoundHandler()
        self.collision_handler = CollisionHandler()
        self.homes = [
            Home(60, 120),
            Home(240, 300),
            Home(420, 480),
            Home(600, 660),
            Home(780, 840),
        ]
    
    def update(self):
        # collision management is managed at the Game class level 
        self.collision_handler.check_collisions(self.frog, self.level.objects)

        # continual updating position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.level.objects:
            object.update()
        
        # if frog y-position less than 180 (in row of home slots), check if frog within home boundaries
        if self.frog_in_home_row():
            self.frog.carry(0)
            self.home_check()

        # continually update frog
        self.frog.update()

    def draw(self):
        self.screen.reset()

        for object in self.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
                    
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))

        for home in self.homes:
            if home.occupied and self.frog.alive:
                self.screen.surface.blit(self.frog.image_home, (((home.bounds[0] + home.bounds[1]) // 2 - self.frog.image_home.get_width() // 2), 124))

        #self.draw_grid()

        pygame.display.flip()

    def draw_grid(self):
        for i in range(0, self.screen.height, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (0, i), (self.screen.width, i))

        for i in range(0, self.screen.width, 60):
            pygame.draw.line(self.screen.surface, (255, 255, 255), (i, 0), (i, self.screen.height))

    def frog_in_home_row(self):
        return self.frog.rect.top < 180
    
    def home_check(self):
        for home in self.homes:
            if self.frog.rect.centerx in range(home.bounds[0], home.bounds[1]):
                home.occupied = True

    def game_over(self):
        return self.lives <= 0