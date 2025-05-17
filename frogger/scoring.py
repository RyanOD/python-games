import pygame
from config import FROG_START_Y, SCREEN_WIDTH, SCREEN_HEIGHT

class Scoring:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.rows = [
            {"visited": False, "value": 0},
            {"visited": False, "value": 100},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
        ]
    
    def update(self, dt):
        row = self.rows[self.game.frog.rect.y // 50 - 1]
        if not row["visited"]:
            self.score += row["value"]
            row["visited"] = True

    def draw(self, screen):
        score_title = pygame.font.Font.render(self.game.screen.font_sm, "1-Up", True, (255, 255, 255))
        score = pygame.font.Font.render(self.game.screen.font_sm, str(self.score), False, (255, 255, 255))
        screen.surface.blit(score_title, (100, 5))
        screen.surface.blit(score, (100, 33))

    def reset_rows(self):
        for row in self.rows:
            row['visited'] = False
    
    def reset(self):
        self.score = 0
        self.reset_rows()