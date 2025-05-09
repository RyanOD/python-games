# Responsibility: Manage state transitions and shared systems.

import pygame
from frog import Frog
from level import Level
from input import InputHandler
from screen import Screen
from sound import SoundHandler
from countdown import Countdown
from collision import CollisionHandler
from frog_manager import *
from scoring import Scoring
from utils import *
from events import event_dispatcher
from state_machine import StateMachine
from state_title import StateTitle
from state_menu import StateMenu
from state_play import StatePlay
from state_play import StatePlay
from state_clear import StateClear
from state_game_over import StateGameOver
from debug import draw_grid

class Game:
    def __init__(self):
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
        self.state_machine.register("title", StateTitle)
        self.state_machine.register("play", StatePlay)
        self.state_machine.register("menu", StateMenu)
        self.state_machine.register("menu", StateMenu)
        self.state_machine.register("clear", StateClear)
        self.state_machine.register("game_over", StateGameOver)

        self.state_machine.change_state("title")

    def update(self, dt):        
        self.state_machine.update(dt)

    def handle_input(self, dt):
        events = pygame.event.get()
        self.state_machine.handle_input(dt, events)

    def draw(self):
        self.state_machine.draw()

    def reset(self):
        self.frog.reset()
        self.scoring.reset()
        self.countdown.reset()
        for home in self.homes:
            home['occupied'] = False
        
    # reset visited state of all rows to False then reset frog
    def reset_level(self):
        for row in self.scoring.rows:
            row['visited'] = False