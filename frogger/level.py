import json
from maps import *
from objects import Object

class Level:
    def __init__(self, level):
        self.level = level

        self.level_map = self.load_data_file('level_data.json')
        self.image_map = self.load_data_file('object_data.json')

        self.objects = self.load_objects(self.level_map)
        self.images = self.load_images()

    def load_data_file(self, filename):
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