from config import *
from config import FROG_START_X, FROG_START_Y

# check if frog y position is within home (goal) row
def frog_in_home_row(frog):
    return frog.rect.top < 150

def frog_in_home_col(frog):
    if (frog.rect.left >= 43 and frog.rect.right <= 107) or (frog.rect.left >= 193 and frog.rect.right <= 257) or (frog.rect.left >= 343 and frog.rect.right <= 407) or (frog.rect.left >= 493 and frog.rect.right <= 557) or (frog.rect.left >= 643 and frog.rect.right <= 707):
        return True
    return False

# check if frog is in water zone
def frog_in_water(frog):
    return WATER_TOP < frog.rect.top < WATER_BOTTOM

# check if frog is in on an object (log or turtle)
def frog_on_object(frog, object):
    overlap = max(0, min(frog.rect.right, object.rect.right) - max(frog.rect.left, object.rect.left))
    return overlap >= frog.rect.width / 2

def frog_hits_boundary(frog, screen):
    if frog.rect.bottom > screen.height - 50:
        frog.rect.bottom = screen.height - 50
    else:
        if frog.rect.left < 0:
            frog.rect.left = 0
            return True
        elif frog.rect.right > SCREEN_WIDTH:
            frog.rect.right = SCREEN_WIDTH
            return True

# the Frog class owns the frog behavior if the frog dies, but not the triggers that kill the frog
def frog_dies(frog):
    frog.carried_speed = 0
    frog.play_sound('die')
    frog.alive = False
    frog.lives -= 1

# when frog dies, begin death_timer countdown and cylce through frog dying images based on time
def frog_dying_animation(frog):
    if frog.death_timer > 0:
        frog.death_timer -= 1
        frog.image = frog.image_dying[min(len(frog.image_dying) - 1, frog.death_timer // frog.death_frame_duration)]
        return False
    return True

# reset the frog based on specified x, y screen positions
def frog_reset(frog):
    frog.image = frog.image_original
    frog.rect.x = FROG_START_X - frog.width * 0.5
    frog.rect.y = FROG_START_Y
    frog.alive = True
    frog.death_timer = frog.death_frame_duration * len(frog.image_dying)