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

        print(frog_safe)
        if frog_safe and frog.rect.top < 150:
            frog.carry(0)

        elif not frog_safe and self.frog_in_water(frog):
            frog.carry(0)
            self.kill_frog(frog)
    
    def resolve_collision(self, frog, object):
        if object.type in ('C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB'):
            self.kill_frog(frog)
            return False
        elif object.type in ('T', 'LL', 'LM', 'LR'):
            if object.rect.left <= frog.rect.centerx <= object.rect.right:
                frog.carry(object.movement)
                return True
        return False
    
    def frog_in_goal(self, frog):
        return frog.rect.top < 180
    
    def frog_in_water(self, frog):
        return frog.rect.top < 480
    
    def kill_frog(self, frog):
        event_dispatcher.dispatch('play_sound', 'die_road')
        frog.lives -= 1
        if frog.rect.left < 0:
            frog.rect.left = 0

        if frog.rect.right > SCREEN_WIDTH:
            frog.rect.right = SCREEN_WIDTH - 14 # right side padding?

        frog.image = frog.image_dead
        frog.alive = False
        if frog.death_timer <= 0:
            frog.reset()