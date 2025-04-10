from objects import Object
from utils import load_data_file, load_objects

class Level:
    def __init__(self, images, level):
        self.level = level
        self.level_map = load_data_file('level_data.json')

        self.images = images
        self.objects = load_objects(self.level_map, self.images, Object)
    
    def update(self):
        for object in self.objects:
            object.update()

    def reset(self):
        self.objects = self.load_objects(self.level)