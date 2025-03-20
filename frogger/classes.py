import pygame
from maps import *
from asset_paths import *

class Screen:
    def __init__(self):
        self.width = 900
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
        self.width = 60
        self.height = 60
        self.x = screen.width / 2 - self.width / 2
        self.y = screen.height - 130
        self.speed = 10

        # load and scale frog image
        self.image_original = pygame.image.load('assets/frog_1.png')
        self.image = pygame.transform.scale(self.image_original, (self.width, self.height))

        # create a rect for frog image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

        # set frog x and y movement rates
        self.movement_x = 60
        self.movement_y = 80
    
    def update(self, direction):
        if direction == "up":
            self.image = pygame.transform.rotate(self.image_original, 0)
            self.y -= self.movement_y
        elif direction == "down":
            self.image = pygame.transform.rotate(self.image_original, 180)
            self.y += self.movement_y
        elif direction == "left":
            self.image = pygame.transform.rotate(self.image_original, 90)
            self.x -= self.movement_x
        elif direction == "right":
            self.image = pygame.transform.rotate(self.image_original, -90)
            self.x += self.movement_x

        self.rect.topleft = (self.x, self.y)

'''GameObject Class manages all game objects besides frogs (vehicles, logs, hedges, etc)'''
class GameObject:
    def __init__(self, x, y, type, width, height, speed, direction, image):
        self.type = type
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction

        # load and scale object image
        self.image_original = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image_original, (self.height, self.width))

        # set object initial x and y positions
        self.x = x
        self.y = y

        # create a rect for object image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed
        
        if self.x < -80:
            self.x = 872
        elif self.x > 872:
            self.x = -80
        
        self.rect.topleft = (self.x, self.y)

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
                    self.objects.append(GameObject(j * 60, i * 80 + 8, **OBJECT_MAP[object]))

class CollisionHandler:
    def check_collisions(self, frog, objects):
        for object in objects:
            if frog.rect.colliderect(object.rect):
                self.resolve_collision(frog, object)

    def resolve_collision(self, frog, object):
        if object.type in ('car', 'dozer'):
            frog.x = 500
            frog.rect.topleft = (500, object.rect.y)
        elif object.type in ('turtle', 'log'):
            frog.x = object.x

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
        self.frog.update("up")

class MoveRightCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("right")

class MoveDownCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("down")

class MoveLeftCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("left")