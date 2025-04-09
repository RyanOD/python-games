# Responsibility: Map key presses to commands and delegate execution of user input

import pygame
from commands import MoveUpCommand, MoveRightCommand, MoveDownCommand, MoveLeftCommand
from events import event_dispatcher
from time_manager import TimeManager

class InputHandler:
    def __init__(self, frog):
        self.commands = {
            #pygame.QUIT: QuitCommand(frog),
            pygame.K_UP: MoveUpCommand(frog),
            pygame.K_RIGHT: MoveRightCommand(frog),
            pygame.K_DOWN: MoveDownCommand(frog),
            pygame.K_LEFT: MoveLeftCommand(frog)
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in self.commands:
            self.commands[event.key].execute()
            event_dispatcher.dispatch('play_sound', 'hop')