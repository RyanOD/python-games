# Responsibility: Detect when a collision happens and resolve associated game events

from frog_manager import *

class CollisionHandler:
    def __init__(self):
        self.unsafe_objects = ['C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB', 'GMT']
        self.safe_objects = ['T', 'LL', 'LM', 'LR']

    def safe_collision(self, frog, objects):
        # check all objects for collision with frog
        for object in objects:
            if frog.rect.colliderect(object.rect) and frog.on_object(object):
                # check to see if frog survives collision (vehicles kill frog...logs and turtles do not)
                return self.resolve_collision(frog, object)
        # if collision check for all objects fails, then check to see if frog is in the water
        if frog.in_water():
            return False
        return True
    
    def resolve_collision(self, frog, object):
        # set frog carry speed to zero and return False if frog collides with vehicle or grass (unsafe objects)
        if object.type in self.safe_objects and frog.on_object(object):
            frog.carried_speed = object.movement
            return True
        return False