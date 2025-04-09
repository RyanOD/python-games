# Responsibility: Detect when a collision happens and resolve associated game events

from events import event_dispatcher
from screen import Screen

class CollisionHandler:
    def check_collisions(self, frog, objects):
        frog_safe = False
        
        # check all objects for collision with frog
        for object in objects:
            if frog.rect.colliderect(object.rect):
                # check to see if frog dies from collision (vehicles kill frog...logs and turtles do not)
                if self.resolve_collision(frog, object):
                    # collision did not kill frog
                    frog_safe = True

        if not frog_safe and frog.in_water():
            frog.carry(0)
            frog.die()
    
    def resolve_collision(self, frog, object):
        # set frog carry speed to zero and return False if frog collides with vehicle or grass
        if object.type in ('C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB'):
            frog.carry(0)
            frog.die()
            return False
        # update frog carry speed and return True if frog collides with turtle or log and is more than half on
        elif object.type in ('T', 'LL', 'LM', 'LR'):
            if object.rect.left <= frog.rect.centerx <= object.rect.right:
                frog.carry(object.movement)
                return True
        # return false if frog is more than half off lor or turtle
        return False