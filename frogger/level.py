from objects import Object
from utils import load_data_file, load_objects
import pygame

class Level:
    def __init__(self, images, level):
        self.timer = 30
        self.level_map = load_data_file('level_data.json')
        self.images = images
        self.load_level(level)
        self.row_value = [
            {"visited": False, "value": 0},
            {"visited": False, "value": 100},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
        ]

    def update(self, dt):
        for object in self.objects:
            object.update(dt)
    
    def draw(self, screen):
        font = pygame.font.Font("assets/upheavtt.ttf", 34)
        level_title = pygame.font.Font.render(font, "Level", True, (255, 255, 255))
        level = pygame.font.Font.render(font, str(self.num), False, (255, 255, 255))
        screen.surface.blit(level_title, (300, 5))
        screen.surface.blit(level, (300, 33))
    
    def load_level(self, level):
        self.num = level
        self.objects = load_objects(self.level_map, self.images, self.num, Object)

    def reset_rows(self):
        for row in self.row_value:
            row['visited'] = False