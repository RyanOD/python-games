# Responsibility: Detect when a collision happens and resolve associated game events

class CollisionHandler:
    def check_collisions(self, frog, lane):
        for object in lane.objects:
            if frog.rect.colliderect(object.rect):
                self.resolve_collision(frog, lane, object)
                return
            
    def resolve_collision(self, frog, lane, object):
        if object.type in ('car', 'dozer'):
            event_dispatcher.dispatch('play_sound', 'die_road')
            frog.alive = False
            frog.image = frog.image_dead
        elif object.type in ('turtle', 'log'):
            frog.x(lane.direction)