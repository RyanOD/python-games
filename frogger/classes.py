import pygame

class Screen:
    def __init__(self):
        self.width = 1200
        self.height = 1200
        self.fill = (255, 0, 255)
        self.title = "Frogger Clone by Retro Clone"
        self.surface = pygame.display.set_mode((self.width, self.height))
    
    def clear(self):
        self.surface.fill(self.fill)

class Frog:
    def __init__(self, screen):
        self.width = 170
        self.height = 120
        self.x = screen.width / 2 - self.width / 2
        self.y = screen.height / 2 - self.height / 2
        self.speed = 10
        self.image = pygame.image.load('assets/frog.png')
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}
    
    def move(self, direction):
        if direction == "up":
            pass
            # set orientation to frog facing up
            # set frog image to extended version
            # move frog one lane forward in a smooth manner
            # set frog image to stationary version
        elif self.orientation == "down":
            pass
        elif self.orientation == "left":
            pass
        elif self.orientation == "right":
            pass

class Log:
    def __init__(self):
        self.x = 100 #FIX THIS
        self.lane = 1 #FIX THIS
        self.speed = 8
    
    def move(self):
        pass

class Turtle:
    def __init__(self):
        self.x = x
        self.lane = lane
        self.speed = 8
    
    def move(self):
        pass

class Vehicle:
    def __init__(self):
        pass

class InputHandler:
    def __init__(self, frog):
        self.commands = {
            pygame.K_UP: MoveUpCommand(frog),
            pygame.K_RIGHT: MoveRightCommand(frog),
            pygame.K_DOWN: MoveDownCommand(frog),
            pygame.K_LEFT: MoveLeftCommand(frog)
        }

    def handle_input(self, pressed_keys):
        for key, command in self.commands.items():
            if pressed_keys[key]:
               command.execute()

class Command:
    def execute(self):
        pass

class MoveUpCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.move("up")

class MoveRightCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.move("right")

class MoveDownCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.move("down")

class MoveLeftCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.move("left")