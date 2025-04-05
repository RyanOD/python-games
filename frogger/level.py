import json
from maps import *
from objects import Object

class Level:
    def __init__(self, level):
        self.level = level
        self.image_map = {
            'F': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'assets/frog_1.png'},
            'FD': {'type': 'frog', 'height': 60, 'width': 60, 'image': 'assets/dead_4.png'},
            'T': {'type': 'turtle', 'height': 60, 'width': 60, 'image': 'assets/turtle_1.png'},
            'LL': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_lt.png'},
            'LM': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_md.png'},
            'LR': {'type': 'log', 'height': 60, 'width': 60, 'image': 'assets/log_rt.png'},
            'TL': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'assets/truck_lt.png'},
            'TR': {'type': 'truck', 'height': 60, 'width': 60, 'image': 'assets/truck_rt.png'},
            'C1': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_1.png'},
            'C2': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_2.png'},
            'C3': {'type': 'car', 'height': 60, 'width': 60, 'image': 'assets/car_3.png'},
            'D': {'type': 'dozer', 'height': 60, 'width': 60, 'image': 'assets/dozer.png'},
            'GTL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_tl.png'},
            'GTR': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_tr.png'},
            'GBR': {'type': 'grass', 'height': 30, 'width': 30, 'image': 'assets/grass_br.png'},
            'GBL': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_bl.png'},
            'GMW': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mw.png'},
            'GMT': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mt.png'},
            'GMB': {'type': 'grass', 'height': 60, 'width': 30, 'image': 'assets/grass_mb.png'},
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
                for col, object_data in enumerate(lane_data['objects']):
                    if object_data:
                        x = col * lane_data['width']
                        y = (row + 1) * lane_data['height']
                        objects.append(Object(object_data, x, y, lane_data['height'], lane_data['width'], lane_data['movement']))
        return objects
    
    def load_images(self):
        return {obj_type: pygame.transform.scale(pygame.image.load(self.image_map[obj_type]['image']), (self.image_map[obj_type]['height'], self.image_map[obj_type]['width'])) for obj_type in self.image_map}
    
    def update(self):
        for object in self.objects:
            object.update()

    def reset(self):
        self.objects = self.load_objects(self.level)