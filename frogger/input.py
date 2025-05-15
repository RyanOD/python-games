# Responsibility: Map key presses to commands and delegate execution of user input

import pygame
from commands import *

class InputHandler:
    def __init__(self, game, dt=0):
        self.commands = {
            pygame.K_UP: MoveUpCommand(),
            pygame.K_RIGHT: MoveRightCommand(),
            pygame.K_DOWN: MoveDownCommand(),
            pygame.K_LEFT: MoveLeftCommand(),
            pygame.K_SPACE: PauseGameCommand()
        }

    def handle_event(self, event, game, dt):
        if event.type == pygame.KEYDOWN and event.key in self.commands:
            self.commands[event.key].execute(game, dt)