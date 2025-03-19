import pygame
from levels import *
from asset_paths import *

class Screen:
    def __init__(self):
        self.width = 840
        self.height = 1020
        self.fill_road = (0, 0, 0)
        self.fill_water = (0, 51, 153)
        self.title = "Frogger Clone by Retro Clone"
        self.surface = pygame.display.set_mode((self.width, self.height))

    def clear(self):
        self.surface.fill(self.fill_water, (0, 0, self.width, 440))
        self.surface.fill(self.fill_road, (0, 440, self.width, self.height))

class Frog:
    def __init__(self, screen):
        self.width = 170
        self.height = 120
        self.x = screen.width / 2 - self.width / 2
        self.y = screen.height - 130
        self.speed = 10
        self.image_original = pygame.transform.scale(pygame.image.load('assets/frog_1.png'), (60, 60))
        self.image = self.image_original
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}
        self.movement = 80
    
    def move(self, direction):
        if direction == "up":
            self.image = pygame.transform.rotate(self.image_original, 0)
            self.y -= self.movement
        elif direction == "down":
            self.image = pygame.transform.rotate(self.image_original, 180)
            self.y += self.movement
        elif direction == "left":
            self.image = pygame.transform.rotate(self.image_original, 90)
            self.x -= self.movement
        elif direction == "right":
            self.image = pygame.transform.rotate(self.image_original, -90)
            self.x += self.movement

'''GameObject Class manages all game objects besides frogs (vehicles, logs, hedges, etc)'''
class GameObject:
    def __init__(self, x, y, type, width, height, speed, direction, image):
        self.type = type
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.image = pygame.transform.scale(pygame.image.load(image), (self.height, self.width))
        self.x = x
        self.y = y

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed
        
        if self.x < -80:
            self.x = 872
        elif self.x > 872:
            self.x = -80

class Level:    
    def __init__(self, number):
        self.data = {}
        self.objects = []
        self.number = number
        self.layout = self.load_level(self.number)
        self.time_limits = [41, 51, 61, 71]
        self.time_limit = self.time_limits[number]
    
    def load_level(self, number):
        self.data = LEVEL_MAP[number - 1]

        for i, lane in enumerate(self.data):
            for j, object in enumerate(lane):
                if object:
                    self.objects.append(GameObject((j + 1) * 60, i * 80 + 8, **OBJECT_MAP[object]))

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