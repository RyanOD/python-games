import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Screen:
    def __init__(self, game):
        self.game = game
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.font_sm = pygame.font.Font("assets/upheavtt.ttf", 34)
        self.font_md_sm = pygame.font.Font("assets/upheavtt.ttf", 60)
        self.font_md = pygame.font.Font("assets/upheavtt.ttf", 100)
        self.font_lg = pygame.font.Font("assets/upheavtt.ttf", 200)

        # set screen window caption
        pygame.display.set_caption("Frogger Clone by Retro Clones")

    def draw(self, bg_image, draw_flags):
        # clear screen
        self.surface.fill((0, 0, 0))

        # render background
        self.surface.blit(bg_image, (0, 0))

        for asset in draw_flags:
            if asset == 'objects':
                for object in self.game.level.objects:
                    if object.image:
                        object.draw(self)
            else:
                attr = getattr(self.game, asset, None)
                if attr:
                    attr.draw(self)