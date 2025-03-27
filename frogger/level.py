
from maps import *
from objects import Object

class Level:
    def __init__(self, level):
        self.level = level
        self.objects = self.load_objects(self.level - 1)

    def load_objects(self, level):
        objects = []
        for lane, lane_info in enumerate(LEVEL_MAP[0]):
            print(lane)
            speed = lane_info['speed']
            direction = lane_info['direction']
            for row, obj_info in enumerate(lane_info['objects']):
                if obj_info:
                    obj = Object(obj_info, row * 60, (lane + 2) * 60, speed, direction)
                    objects.append(obj)
        return objects

    def update(self, delta_time):
        for object in self.objects:
            object.update()

    def reset(self):
        self.objects = self.load_objects(self.level)