import pygame

class Screen:
    def __init__(self):
        self.width = 800
        self.height = 800
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
        self.image_original = pygame.transform.scale(pygame.image.load('assets/frog.png'), (80, 80))
        self.image = self.image_original
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}
        self.movement = 40
    
    def move(self, direction):
        if direction == "up":
            self.image = pygame.transform.rotate(self.image_original, 0)
            self.y -= self.movement
        elif direction == "down":
            self.image = pygame.transform.rotate(self.image_original, 180)
            self.y += self.movement
        elif direction == "left":
            self.image = pygame.transform.rotate(self.image_original, 270)
            self.x -= self.movement
        elif direction == "right":
            self.image = pygame.transform.rotate(self.image_original, 90)
            self.x += self.movement

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

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in self.commands:
            self.commands[event.key].execute()

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