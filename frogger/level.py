from objects import Object
from utils import load_data_file, load_objects

class Level:
    def __init__(self, game, images, level):
        self.game = game
        self.level = level
        self.timer = 30
        self.level_map = load_data_file('level_data.json')

        self.images = images
        self.objects = load_objects(self.level_map, self.images, Object)
    
    def update(self, dt):
        #for object in self.objects:
            #object.update()
        
        # update x-position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.objects:
            if not self.game.screen.on_screen(object):
                object.reset(self.game.screen)
            object.update(dt)

    def reset(self):
        self.objects = self.load_objects(self.level)