import pygame
from maps import *

class Screen:
    def __init__(self):
        self.width = 900
        self.height = 1080
        self.lane_padding = 6
        self.lane_height = 64
        self.lane_width = 64
        self.caption = self.set_caption("Frogger Clone by Retro Clone")
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.bg = self.get_bg("assets/bg.png")

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_bg(self, bg_image):
        # Load the image
        return pygame.image.load(bg_image).convert()
    '''
    def frog_boundary_check(self, frog):
        # screen boundary check / adjustment
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.width:
            self.rect.right = self.width - 14 # right side padding?
        elif self.rect.y > self.height:
            self.rect.y = self.height - frog.height * 3
    
    def object_boundary_check(self, object):
        if object.rect.x < -self.width or object.rect.x > self.width + object.width:
            object.rect.x = self.width - object.rect.x
    '''
    def on_screen(self, sprite):
        return 0 < sprite.rect.centerx < self.width