import pygame

class Screen:
    def __init__(self):
        self.width = 792
        self.height = 1050
        self.fill_road = (0, 0, 0)
        self.fill_water = (65, 107, 223)
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
        self.y = screen.height - 160
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
    def __init__(self, type, width, height, speed, x, y, direction, image):
        self.type = type
        self.width = width
        self.height = height
        self.speed = speed
        self.x = x
        self.y = y
        self.direction = direction
        self.image = pygame.transform.scale(pygame.image.load(image), (self.height, self.width))

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed
        
        if self.x < -80:
            self.x = 872


class Level:
    def __init__(self, number):
        self.number = number
        self.layout = self.get_layout(self.number)
        self.time_limits = [41, 51, 61, 71]
        self.time_limit = self.time_limits[number]
    
    def get_layout(number):
        if number == 1:
            return [
                ["G", "G", "G", "G", "G"],  # Goal zone (G)
                ["L", "L", "T", "L", "L"],  # Water with logs (L) and turtles (T)
                ["L", "A", "L", "L", "L"],  # Water with an alligator (A)
                ["S", "S", "S", "S", "S"],  # Safe zone (S)
                ["C", " ", "T", " ", "C"],  # Road with cars (C) and trucks (T)
                ["C", "M", " ", "M", "C"],  # Road with cars (C) and motorcycles (M)
                ["S", "S", "S", "S", "S"],  # Safe zone
                ["F", "F", "F", "F", "F"],  # Frog start position (F)
            ]

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