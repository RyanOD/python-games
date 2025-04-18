# Responsibility: Detect when a collision happens and resolve associated game events

class CollisionHandler:
    unsafe_objects = ('C1', 'C2', 'C3', 'D', 'TR', 'TL', 'GBL', 'GTL', 'GBR', 'GTR', 'GBL', 'GMW', 'GMB')
    safe_objects = ('T', 'LL', 'LM', 'LR')

    def check_collisions(self, frog, objects):
        frog_safe = False
        
        # check all objects for collision with frog
        for object in objects:
            if frog.rect.colliderect(object.rect):

                # check to see if frog survives collision (vehicles kill frog...logs and turtles do not)
                if self.resolve_collision(frog, object):

                    # collision did not kill frog
                    frog_safe = True

        # frog dies because in water and not on a log or turtle
        if not frog_safe and frog.alive and frog.in_water():
            frog.die()
        else:
            frog_safe = True
    
    def resolve_collision(self, frog, object):
        # set frog carry speed to zero and return False if frog collides with vehicle or grass (unsafe objects)
        if object.type in self.unsafe_objects:
            if frog.alive:
                frog.die()
            return False
        
        # update frog carry speed and return True if frog collides with turtle or log and is more than half on (safe objects)
        elif object.type in self.safe_objects:
            if object.rect.left <= frog.rect.centerx <= object.rect.right:
                frog.carried_speed = object.movement
                return True
            
        # return false if frog is more than half off log or turtle
        return False