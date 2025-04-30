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
        self.timer_width = 360
        self.time_tracker = 0
    
    def update(self, dt):
        row = self.rows[self.game.frog.rect.y // 50 - 1]
        if not row["visited"]:
            self.score += row["value"]
            row["visited"] = True
        self.time_tracker += dt 
        if self.time_tracker > 1:
            self.timer_width -= 6
            self.time_tracker = 0

    def draw(self, screen):
        # convert dt into pixels and draw timer bar based on dt
        # pygame.draw.rect(game.screen.surface, (63, 232, 71), (500 + 200 - self.timer_width, SCREEN_HEIGHT - 40, self.timer_width, 30))
        
        font = pygame.font.Font("assets/upheavtt.ttf", 34)
        score_title = pygame.font.Font.render(font, "1-Up", True, (255, 255, 255))
        score = pygame.font.Font.render(font, str(self.score), False, (255, 255, 255))
        screen.surface.blit(score_title, (100, 5))
        screen.surface.blit(score, (100, 33))

    def reset(self):
        for row in self.rows:
            row['visited'] = False