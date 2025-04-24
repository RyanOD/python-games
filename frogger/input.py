# Responsibility: Map key presses to commands and delegate execution of user input

import pygame
from commands import MoveUpCommand, MoveRightCommand, MoveDownCommand, MoveLeftCommand

class InputHandler:
    def __init__(self, frog, dt=0):
        self.commands = {
            pygame.K_UP: MoveUpCommand(frog, dt),
            pygame.K_RIGHT: MoveRightCommand(frog, dt),
            pygame.K_DOWN: MoveDownCommand(frog, dt),
            pygame.K_LEFT: MoveLeftCommand(frog, dt)
        }

    def handle_event(self, event, dt):
        if event.type == pygame.KEYDOWN and event.key in self.commands:
            self.commands[event.key].execute(dt)