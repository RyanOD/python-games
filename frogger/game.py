import pygame
from frog import Frog
from level import Level
from input import InputHandler
from screen import Screen
from sound import SoundHandler
from collision import CollisionHandler
from utils import *
from events import event_dispatcher

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.lives = 3
        self.screen = Screen()
        self.image_data = load_data_file('object_data.json')
        self.images = load_images(self.image_data)
        self.level = Level(self.images, 1)
        self.sound_handler = SoundHandler()
        self.frog = Frog(self.images, self.screen.width // 2, 16 * self.screen.lane_height + self.screen.lane_padding, lambda sound_name: event_dispatcher.dispatch('play_sound', sound_name))
        self.surface = self.screen.surface
        self.input_handler = InputHandler(self.frog)
        self.collision_handler = CollisionHandler()
        self.score = 0
        self.homes = [
            {'occupied': False, 'xl': 60, 'xr': 120},
            {'occupied': False, 'xl': 240, 'xr': 300},
            {'occupied': False, 'xl': 420, 'xr': 480},
            {'occupied': False, 'xl': 600, 'xr': 660},
            {'occupied': False, 'xl': 780, 'xr': 840},
        ]
        self.scoring = [
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
            {"visited": False, "value": 100},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
        ]
    
    def update(self):
        # collision management is managed at the Game class level 
        self.collision_handler.check_collisions(self.frog, self.level.objects)

        # continual updating position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.level.objects:
            if not self.screen.on_screen(object):
                object.reset(self.screen)
            object.update()
        
        # if frog y-position less than 180 (in row of home slots), check if frog within home boundaries

        # continually update frog
        if not self.frog.alive:
            if self.frog.death_timer > 0:
                self.frog.death_timer -= 1
            else:
                self.reset_frog()
        self.frog.update()

        # continually check to see if frog crosses screen boundaries
        if self.frog.alive and not self.screen.on_screen(self.frog):
            self.frog.die()

    def points(self):
        row = self.scoring[self.frog.rect.y // 50 - 1]
        print(self.frog.rect.y // 50 - 1)
        if not row["visited"]:
            self.score += row["value"]
            row["visited"] = True

    def draw(self):
        self.screen.reset()

        for object in self.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
                    
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))

        for f in range(0, self.frog.lives):
            self.screen.surface.blit(self.frog.menu_image, (f * 60 + 10, 850 + self.screen.lane_padding))

        for home in self.homes:
            if home['occupied'] and self.frog.alive:
                self.screen.surface.blit(self.frog.image_home, (((home['xl'] + home['xr']) // 2 - self.frog.image_home.get_width() // 2), 124))

        self.screen.score(self.score)
        pygame.display.flip()

    def frog_in_home_row(self):
        return self.frog.rect.top < 180

    def home_check(self):
        for home in self.homes:
            if self.frog.rect.centerx in range(home['xl'], home['xr']):
                home['occupied'] = True

    def reset_frog(self):
        self.frog.reset(self.screen.width // 2, 16 * self.screen.lane_height + self.screen.lane_padding)
    
    def game_over(self):
        return self.lives <= 0