import pygame
from command import *

class InputHandler:
    def __init__(self, paddle, screen, ball, game):
        self.commands = {
            pygame.K_RETURN: StartGameCommand(),
            pygame.K_SPACE: ServeBallCommand(ball),
            pygame.K_w: MoveUpCommand(paddle, screen),
            pygame.K_s: MoveDownCommand(paddle, screen),
        }
    
    def handle_input(self, pressed_keys):
        for key, command in self.commands.items():
            if pressed_keys[key]:
                command.execute()

'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


        if pressed[pygame.K_w]:
            self.key_up = True
            # paddle_lt.move("up", screen)
        elif pressed[pygame.K_s]:
            self.key_down = True
            # paddle_lt.move("down", screen)
'''