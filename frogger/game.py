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
        # initialize Pygame
        pygame.init()

        # initialize Pygame Screen class and create surface
        self.screen = Screen()
        self.surface = self.screen.surface

        # load image data and game sprite images
        self.image_data = load_data_file('object_data.json')
        self.images = load_images(self.image_data)

        # pass images to level builder to create level objects (vehicles, logs, turtles)
        self.level = Level(self.images, 1)

        # delegate sound management to SoundHandler class
        self.sound_handler = SoundHandler()

        # create instance of Frog class
        self.frog = Frog(
            self.images,
            self.screen.width // 2,
            16 * self.screen.lane_height + self.screen.lane_padding,
            lambda sound_name: event_dispatcher.dispatch('play_sound', sound_name)
        )

        # set frog lives
        self.lives = 3

        # delegate input management to InputHandler class
        self.input_handler = InputHandler(self.frog)

        # delegate object collision management to CollisionHandler class
        self.collision_handler = CollisionHandler()

        # delegate score management to Scoring class
        self.scoring = Scoring(self.frog)

        # set up array to manage state of home goal locations
        self.homes = [
            {'occupied': False, 'xl': 50, 'xr': 100},
            {'occupied': False, 'xl': 200, 'xr': 250},
            {'occupied': False, 'xl': 350, 'xr': 400},
            {'occupied': False, 'xl': 500, 'xr': 550},
            {'occupied': False, 'xl': 650, 'xr': 700},
        ]
    
    def update(self):
        # delegate frog/object collision management to CollisionHandler class
        self.collision_handler.check_collisions(self.frog, self.level.objects)

        # update x-position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.level.objects:
            if not self.screen.on_screen(object):
                object.reset(self.screen)
            object.update()

        # delegate scoring display management to Scoring class
        self.scoring.update()

        # delegate frog position management to Frog class
        self.frog.update()

        # update frog life status based on screen boundary collision
        if self.frog.alive and not self.screen.on_screen(self.frog):
            self.frog.die()

        # check to see if frog makes it to home goal location
        self.home_check()

        # when frog dies, begin death_timer countdown and rotate frog dying images based on time then reset level
        if not self.frog.alive:
            if self.frog.animate():
                self.reset_level()

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
                self.screen.surface.blit(self.frog.image_home, (((home['xl'] + home['xr']) // 2 - self.frog.image_home.get_width() // 2), 104))

        # draw player display
        self.screen.score(self.scoring.score)

        # flip the screen to display all of the above
        pygame.display.flip()

    # check if frog y position is within home (goal) row
    def frog_in_home_row(self):
        return self.frog.rect.top < 150

    # check if frog rect is in the goal home row and if so, update home occupied state to True and reset level
    def home_check(self):
        for home in self.homes:
            if self.frog.rect.centerx in range(home['xl'], home['xr']) and self.frog_in_home_row():
                home['occupied'] = True
                self.reset_level()

    # reset visited state of all rows to False then reset frog
    def reset_level(self):
        for row in self.scoring.rows:
            row['visited'] = False
        self.frog.reset(self.screen.width // 2, 16 * self.screen.lane_height + self.screen.lane_padding)
    
    # end game if all frog lives lost
    def game_over(self):
        return self.lives == 0