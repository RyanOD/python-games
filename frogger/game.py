# Responsibility: Manage state transitions and shared systems.

import pygame
from frog import Frog
from lives import Lives
from level import Level
from input import InputHandler
from screen import Screen
from sound_handler import SoundHandler
from countdown import Countdown
from collision import CollisionHandler
from frog_manager import *
from scoring import Scoring
from utils import *
from state_machine import StateMachine
from config import FROG_LIVES

class Game:
    def __init__(self, level):
        # initialize Pygame
        pygame.init()

        self.active = True
        
        # initialize Pygame Screen class and create surface
        self.screen = Screen(self)
        self.surface = self.screen.surface

        # delegate sound management to SoundHandler class
        self.sound_handler = SoundHandler()

        self.countdown = Countdown()

        # load image data and game sprite images
        self.image_data = load_data_file('object_data.json')
        self.images = load_images(self.image_data)

        # pass images to level builder to create level objects (vehicles, logs, turtles)
        self.level = Level(self.images, level)

        # create instance of Frog class
        self.lives = Lives(self.images)
        self.frog = Frog(self.lives, self.images)

        # delegate input management to InputHandler class
        self.input_handler = InputHandler()

        # delegate object collision management to CollisionHandler class
        self.collision_handler = CollisionHandler()

        # delegate score management to Scoring class
        self.scoring = Scoring(self)

        # set up array to manage state of home goal locations
        self.homes = [
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
            {'occupied': False},
        ]
        # initialize state machine
        self.state_machine = StateMachine(self)

        self.state_machine.change_state("title")

    def update(self, dt):
        self.state_machine.update(dt)

    def handle_input(self, dt):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.active = False
        self.state_machine.handle_input(dt, events)

    def draw(self):
        self.state_machine.draw()

    def reset(self):
        self.frog.reset()
        self.lives.num = FROG_LIVES
        self.scoring.reset()
        self.countdown.reset()
        self.level.num = 1
        for home in self.homes:
            home['occupied'] = False
        if self.level.num == 1:
            self.scoring.score = 0
    
    def load_level(self, level):
        self.level.objects.clear()
        self.level.load_level(level)
        self.reset()

    # reset visited state of all rows to False then reset frog
    def reset_level(self):
        self.countdown.reset()
        for row in self.level.row_values:
            row['visited'] = False