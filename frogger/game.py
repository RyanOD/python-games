import pygame
from frog import Frog
from level import Level
from input import InputHandler
from screen import Screen
from sound import SoundHandler
from collision import CollisionHandler
from scoring import Scoring
from utils import *
from events import event_dispatcher
from debug import draw_grid

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
        self.scoring = Scoring(self.frog)
        self.score = 0
        self.homes = [
            {'occupied': False, 'xl': 50, 'xr': 100},
            {'occupied': False, 'xl': 200, 'xr': 250},
            {'occupied': False, 'xl': 350, 'xr': 400},
            {'occupied': False, 'xl': 500, 'xr': 550},
            {'occupied': False, 'xl': 650, 'xr': 750},
        ]
    
    def update(self):
        # delegate frog/object collision management to CollisionHandler class
        self.collision_handler.check_collisions(self.frog, self.level.objects)

        # update x-position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.level.objects:
            if not self.screen.on_screen(object):
                object.reset(self.screen)
            object.update()
        
        # when frog dies, begin death_timer countdown
        if not self.frog.alive:
            if self.frog.death_timer > 0:
                self.frog.death_timer -= 1
            else:
                self.reset_frog()

        # delegate scoring display management to Scoring class
        self.scoring.update()

        # delegate frog position management to Frog class
        self.frog.update()

        # update frog life status based on screen boundary collision
        if self.frog.alive and not self.screen.on_screen(self.frog):
            self.frog.die()

        # draw all game assets
        self.draw()

    def draw(self):
        # clear the screen
        self.screen.reset()

        # draw all objects (vehicles, logs, turtles) based on level_map data file
        for object in self.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
        
        # if frog image is valid, draw frog image on the screen at frog.rect x, y position
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))

        # draw small frog image below starting row for each frog live left
        for f in range(0, self.frog.lives):
            self.screen.surface.blit(self.frog.menu_image, (f * 60 + 10, 850 + self.screen.lane_padding))

        # draw happy frog image in every home position that player has successfully reached
        for home in self.homes:
            if home['occupied']:
                self.screen.surface.blit(self.frog.image_home, (((home['xl'] + home['xr']) // 2 - self.frog.image_home.get_width() // 2), 124))

        for home in self.homes:
            print(home['occupied'])

        # draw player display
        self.screen.score(self.scoring.score)

        draw_grid(self.screen)
        
        # flip the screen to display all of the above
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