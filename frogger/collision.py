# Responsibility: Detect when a collision happens and resolve associated game events

from events import event_dispatcher

class CollisionHandler:
    def check_collisions(self, frog, objects):
        for object in objects:
            if frog.rect.colliderect(object.rect):
                self.resolve_collision(frog, object)
                return
            else:
                frog.carry(0)
            
    def resolve_collision(self, frog, object):
        if object.type in ('C1', 'C2', 'C3', 'D', 'TR', 'TL'):
            frog.alive = False
            event_dispatcher.dispatch('play_sound', 'die_road')
        elif object.type in ('T', 'LL', 'LM', 'LR'):
            frog.carry(object.movement)