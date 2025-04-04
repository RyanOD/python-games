# Responsibility: Detect when a collision happens and resolve associated game events

from events import event_dispatcher
from maps import SCREEN_WIDTH

class CollisionHandler:
    def check_collisions(self, frog, objects):
        frog_safe = False
        
        for object in objects:
            if frog.rect.colliderect(object.rect):
                if self.resolve_collision(frog, object):
                    frog_safe = True

        if self.frog_in_home(frog):
            frog.carry(0)

        elif not frog_safe and self.frog_in_water(frog):
            frog.carry(0)
            frog.die()
    
    def resolve_collision(self, frog, object):
        if object.type in ('C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB'):
            frog.die()
            return False
        elif object.type in ('T', 'LL', 'LM', 'LR'):
            if object.rect.left <= frog.rect.centerx <= object.rect.right:
                frog.carry(object.movement)
                return True
        return False
    
    def frog_in_home(self, frog):
        return frog.rect.top < 150
    
    def frog_in_water(self, frog):
        return 150 < frog.rect.top < 480