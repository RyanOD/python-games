import pygame
from maps import *
from asset_paths import *

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.fill_road = BLACK
        self.fill_water = BLUE
        self.caption = "Frogger Clone by Retro Clone"
        self.surface = pygame.display.set_mode((self.width, self.height))

    def reset(self):
        self.surface.fill(self.fill_water, (0, 0, self.width, 440))
        self.surface.fill(self.fill_road, (0, 440, self.width, self.height))
        pygame.display.set_caption(self.caption)

class Frog:
    def __init__(self, screen):
        self.alive = True
        self.width = OBJECT_WIDTH
        self.height = OBJECT_HEIGHT
        self.x = screen.width // 2 - self.width // 2
        self.y = 15 * LANE_HEIGHT + LANE_PADDING
        self.speed = 10

        # load and scale frog image
        self.image_original = pygame.transform.scale(pygame.image.load('assets/frog_1.png'), (self.width, self.height))
        self.image = self.image_original
        self.image_dead = pygame.transform.scale(pygame.image.load('assets/dead_4.png'), (self.width, self.height))

        # create a rect for frog image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x + OBJECT_WIDTH // 2, self.y + OBJECT_HEIGHT // 2)
        
        # set and track frog sprite orientation
        self.orientation = "up"
        self.orientations = {"up": 0, "right": 90, "down": 180, "left": 270}

        # set frog x and y movement rates
        self.movement_x = 60
        self.movement_y = 60
    
    def update(self, direction):
        if self.alive:
            if direction == "up":
                self.image = pygame.transform.rotate(self.image_original, 0)
                self.rect.y -= self.movement_y
            elif direction == "down":
                self.image = pygame.transform.rotate(self.image_original, 180)
                self.rect.y += self.movement_y
            elif direction == "left":
                self.image = pygame.transform.rotate(self.image_original, 90)
                self.rect.x -= self.movement_x
            elif direction == "right":
                self.image = pygame.transform.rotate(self.image_original, -90)
                self.rect.x += self.movement_x

class Level:
    def __init__(self, level):
        self.level = level
        self.objects = self.load_objects(self.level - 1)

    def load_objects(self, level):
        objects = []
        for lane_info in LEVEL_MAP[0]:
            speed = lane_info['speed']
            direction = lane_info['direction']
            for obj_info in lane_info['objects']:
                if obj_info:
                    obj = Object(obj_info, 80, 60, speed, direction)
                    objects.append(obj)
        return objects

    def update(self, delta_time):
        for object in self.objects:
            object.update()

    def reset(self):
        self.objects = self.load_objects(self.level)

class Object:
    def __init__(self, type, x, y, speed, direction):
        self.type = type
        self.x = x
        self.y = y
        self.image_original = pygame.image.load(OBJECT_MAP[self.type]['image'])
        self.image = pygame.transform.scale(self.image_original, (OBJECT_HEIGHT, OBJECT_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed
        self.direction = direction
    
    def update(self, delta_time):
        if self.direction == 'left':
            self.rect.x -= self.speed * delta_time
        else:
            self.rect.x += self.speed * delta_time

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0

class SoundHandler:
    def __init__(self):
        self.mixer = pygame.mixer.init()
        self.sounds = {
            'hop': pygame.mixer.Sound('assets/hop.mp3'),
            'die_road': pygame.mixer.Sound('assets/die_road.mp3')
        }
        self.sound_commands = {
            'hop': PlayHopSoundCommand(self.handle_sound),
            'die_road': PlayRoadDeathSoundCommand(self.handle_sound),
        }
        for sound in self.sounds.values():
            sound.set_volume(0.5)

        event_dispatcher.register("play_sound", self.handle_sound)

    def handle_sound(self, sound):
        if(sound in self.sounds):
            self.sounds[sound].play()

class PlayHopSoundCommand:
    def __init__(self, sound_handler):
        self.sound_handler = sound_handler

    def execute(self):
        self.sound_handler.handle_sound('hop')

class PlayRoadDeathSoundCommand:
    def __init__(self, sound_handler):
        self.sound_handler = sound_handler

    def execute(self):
        self.sound_handler.handle_sound('die_road')

class CollisionHandler:
    def check_collisions(self, frog, lane):
        for object in lane.objects:
            if frog.rect.colliderect(object.rect):
                self.resolve_collision(frog, lane, object)
                return
            
    def resolve_collision(self, frog, lane, object):
        if object.type in ('car', 'dozer'):
            event_dispatcher.dispatch('play_sound', 'die_road')
            frog.alive = False
            frog.image = frog.image_dead
        elif object.type in ('turtle', 'log'):
            frog.x(lane.direction)

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
            event_dispatcher.dispatch('play_sound', 'hop')

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

class EventDispatcher:
    def __init__(self):
        self.listeners = {}
    
    def register(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def dispatch(self, event_type, *args, **kwargs):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(*args, **kwargs)

# Global event dispatcher
event_dispatcher = EventDispatcher()

# Observable base class
class Observable:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observers(self, observer):
        self.observers.remove(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

# Observer base class
class Observer:
    def update(self, *args, **kwargs):
        pass