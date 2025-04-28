import pygame
from utils import load_data_file
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Screen:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.lane_padding = 6
        self.lane_height = 50
        self.lane_width = 50
        self.caption = self.set_caption("Frogger Clone by Retro Clone")
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.bg = self.get_bg("assets/bg.png")

    def reset(self):
        # using a background image here instead of multiple surface.fill() calls
        self.surface.blit(self.bg, (0, 0))

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_bg(self, bg_image):
        # Load the background image
        return pygame.image.load(bg_image).convert()
    
    def score(self, player_score):
        font = pygame.font.Font("assets/upheavtt.ttf", 34)
        score_title = pygame.font.Font.render(font, "1-Up", True, (255, 255, 255))
        score = pygame.font.Font.render(font, str(player_score), False, (255, 255, 255))
        self.surface.blit(score_title, (100, 5))
        self.surface.blit(score, (100, 33))