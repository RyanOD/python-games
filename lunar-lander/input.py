import pygame
from command import AccelerateCommand, RotateCWCommand, RotateCCWCommand

class InputHandler:
    def __init__(self, ship):
        self.commands = {
            pygame.K_UP: AccelerateCommand(ship),
            pygame.K_RIGHT: RotateCWCommand(ship),
            pygame.K_LEFT: RotateCCWCommand(ship)
        }
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in self.commands:
            self.commands[event.key].execute()