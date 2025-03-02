import pygame

'''
The Command design pattern sets up an innerstitial Class responsible for interacting with the game loop and the various game responses to user input. This design pattern decouples the game loop from the game response to user input making it easier to add new input options and responses.

Consider the following two resources to learn more about the Command design pattern:
- https://gameprogrammingpatterns.com/command.html
- https://refactoring.guru/design-patterns/command

'''

class Command:
    def execute(self):
        pass

class StartGameCommand(Command):
    pass

class ServeBallCommand(Command):
    def __init__(self, ball):
        self.ball = ball

    def execute(self):
        self.ball.serve()

class MoveUpCommand(Command):
    def __init__(self, paddle, screen):
        self.paddle = paddle
        self.screen = screen
    
    def execute(self):
        self.paddle.move("up", self.screen)

class MoveDownCommand(Command):
    def __init__(self, paddle, screen):
        self.paddle = paddle
        self.screen = screen

    def execute(self):
        self.paddle.move("down", self.screen)

class PauseGameCommand(Command):
    def execute(game):
        pass

class QuitGameCommand(Command):
    def execute():
        pygame.quit()
        exit()
