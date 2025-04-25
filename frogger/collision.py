# Responsibility: Detect when a collision happens and resolve associated game events

class CollisionHandler:
    unsafe_objects = ('C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB')
    safe_objects = ('T', 'LL', 'LM', 'LR')

    def check_collisions(self, frog, objects):
        frog_safe = False
        
        # check all objects for collision with frog
        for object in objects:
            if frog.rect.colliderect(object.rect) and frog.alive:
                # check to see if frog survives collision (vehicles kill frog...logs and turtles do not)
                frog_safe = self.resolve_collision(frog, object)
        return frog_safe
    
    def resolve_collision(self, frog, object):
        # set frog carry speed to zero and return False if frog collides with vehicle or grass (unsafe objects)
        if frog.in_water():
                frog.carried_speed = object.movement
                return True
        else:
            frog.carried_speed = 0
            frog.die()
            return False