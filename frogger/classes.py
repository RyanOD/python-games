import pygame

class Screen:
    def __init__(self):
        self.width = 1200
        self.height = 1200
        self.fill = (255, 255, 255)
        self.title = "Frogger Clone by Retro Clone"
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        pygame.display.set_caption(self.title)
        pygame.display.flip()
    
    def clear(self):
        self.surface.fill(self.fill)

class Frog:
    def __init__(self, screen):
        self.x = screen.width / 2
        self.y = screen.height - 50
        self.speed = 10
        self.image = pygame.image.load('assets/frog.png')
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

    def draw(self, screen):
        screen.surface.blit(self.image, (self.x, self.y))
    
    def move(self):
        if self.orientation == "up":
            pass
            # set orientation to frog facing up
            # switch stationary frog image to extended from image
            # move frog one lane forward in a smooth manner
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
'''
class InputHandler:
    def __init__(self):
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
    def __init__():
        pass

    def MoveUpCommand(self, frog):
        def __init__():
            self.frog = frog

        def execute(self):
            self.frog.move("up")
    
    def MoveRightCommand(self, frog):
        def __init__():
            self.frog = frog

        def execute(self):
            self.frog.move("right")

    def MoveDownCommand(self, frog):
        def __init__():
            self.frog = frog

        def execute(self):
            self.frog.move("down")

    def MoveLeftCommand(self, frog):
        def __init__():
            self.frog = frog

        def execute(self):
            self.frog.move("left")
            '''