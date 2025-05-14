import pygame
from events import event_dispatcher
from state_game import StateGame
from config import SCREEN_WIDTH

class StateWelcome(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()

    def enter(self):
        self.timer = 300

    def update(self, dt = None, events = None):
        if self.timer > 0:
            self.game.level.update(dt)
            self.timer -= dt * 100
        else:
            self.game.state_machine.change_state("play")

    def handle_input(self, dt = None, events = None):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.draw(self.bg_image, self.game.level.objects, self.game.frog, self.game.scoring, self.game.countdown, self.game.level)
        if self.timer > 50:
            pygame.draw.rect(self.game.screen.surface, (10, 10, 10), (SCREEN_WIDTH // 2 - 50, 405, 100, 40))
            font = pygame.font.Font("assets/upheavtt.ttf", 34)
            game_over_text = pygame.font.Font.render(font, str(int(self.timer // 100) + 1), True, (255, 255, 255))
            self.game.screen.surface.blit(game_over_text, (SCREEN_WIDTH // 2 - 2, 407))
        
    def exit(self):
        pass