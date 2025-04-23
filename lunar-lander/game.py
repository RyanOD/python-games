import pygame
import random
from landscape_data import VERTICES, LANDINGS

from ship import Ship
from screen import Screen
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_HEIGHT, SHIP_WIDTH
from input import InputHandler
from state_machine import StateMachine
from state_title import StateTitle
from landscape import Landscape

class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.ship = Ship()
        self.landscape = Landscape()
        self.screen = Screen()
        self.input_handler = InputHandler(self.ship)
        self.start_x = 10
        self.start_y = 10

        # initialize state machine
        self.state_machine = StateMachine()
        self.state_machine.change_state(StateTitle(self))

    def update(self, dt):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.ship.lives = 0
            elif self.ship.alive:
                self.input_handler.handle_event(event)
    
        self.state_machine.update(dt, events)

    def handle_input(self):
        self.state_machine.handle_input()
        
    def draw(self):
        self.state_machine.draw()

    def game_over(self):
        return self.ship.lives <= 0