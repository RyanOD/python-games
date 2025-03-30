import json
from maps import *
from objects import Object

class Level:
    def __init__(self, level):
        self.level = level
        self.image_map = {
            'F': {'type': 'frog', 'image': 'assets/frog_1.png'},
            'FD': {'type': 'frog', 'image': 'assets/dead_4.png'},
            'T': {'type': 'turtle', 'image': 'assets/turtle_1.png'},
            'LL': {'type': 'log', 'image': 'assets/log_lt.png'},
            'LM': {'type': 'log', 'image': 'assets/log_md.png'},
            'LR': {'type': 'log', 'image': 'assets/log_rt.png'},
            'TL': {'type': 'truck', 'image': 'assets/truck_lt.png'},
            'TR': {'type': 'truck', 'image': 'assets/truck_rt.png'},
            'C1': {'type': 'car', 'image': 'assets/car_1.png'},
            'C2': {'type': 'car', 'image': 'assets/car_2.png'},
            'C3': {'type': 'car', 'image': 'assets/car_3.png'},
            'D': {'type': 'dozer', 'image': 'assets/dozer.png'},
            'GTR': {'type': 'grass_top_right', 'image': 'assets/grass_tr.png'},
            'GBM': {'type': 'grass_top_right', 'image': 'assets/grass_bm.png'},
            'GTL': {'type': 'grass_top_right', 'image': 'assets/grass_tl.png'},
            'GMM': {'type': 'grass_top_right', 'image': 'assets/grass_mm.png'},
        }
        self.level_map = self.load_level_map('levels.json')
        self.objects = self.load_objects(self.level_map)
        self.images = self.load_images()

    def load_level_map(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)
    
    def load_objects(self, level_map):
        objects = []
        for level_data in level_map['levels']:
            for row, lane_data in enumerate(level_data['lanes']):
                movement = lane_data['movement']
                for col, object_data in enumerate(lane_data['objects']):
                    if object_data:
                        x = col* 60
                        y = (row + 2) * 60
                        objects.append(Object(object_data, x, y, movement))
        return objects
    
    def load_images(self):
        return {obj_type: pygame.transform.scale(pygame.image.load(self.image_map[obj_type]['image']), (OBJECT_HEIGHT, OBJECT_WIDTH)) for obj_type in self.image_map}
    
    def update(self):
        for object in self.objects:
            object.update()

    def reset(self):
        self.objects = self.load_objects(self.level)