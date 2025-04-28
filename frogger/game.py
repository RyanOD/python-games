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
from state_machine import StateMachine
from state_title import StateTitle
from state_play import StatePlay
from debug import draw_grid

class Game:
    def __init__(self):
        # initialize Pygame
        pygame.init()

        # initialize Pygame Screen class and create surface
        self.screen = Screen()
        self.surface = self.screen.surface

        # delegate sound management to SoundHandler class
        self.sound_handler = SoundHandler()


        # load image data and game sprite images
        self.image_data = load_data_file('object_data.json')
        self.images = load_images(self.image_data)

        # pass images to level builder to create level objects (vehicles, logs, turtles)
        self.level = Level(self, self.images, 1)

        # create instance of Frog class
        self.frog = Frog(
            self.images,
            lambda sound_name: event_dispatcher.dispatch('play_sound', sound_name)
        )

        # delegate input management to InputHandler class
        self.input_handler = InputHandler(self.frog)

        # delegate object collision management to CollisionHandler class
        self.collision_handler = CollisionHandler()

        # delegate score management to Scoring class
        self.scoring = Scoring(self.frog)

        # set up array to manage state of home goal locations
        self.homes = [
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
        ]
        # initialize state machine
        self.state_machine = StateMachine()
        self.state_machine.change_state(StatePlay(self))

    def update(self, dt):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                    self.frog.lives = 0
            elif self.frog.alive:
                    self.input_handler.handle_event(event, dt)
        
        self.state_machine.update(dt, events)

    def handle_input(self):
        self.state_machine.handle_input()

    def draw(self):
        self.state_machine.draw()
    
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
        return self.frog.lives == 0