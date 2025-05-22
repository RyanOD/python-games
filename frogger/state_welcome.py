import pygame
from state_game import StateGame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class StateWelcome(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()
        self.draw_flags = ['background', 'objects', 'frog', 'scoring', 'countdown', 'level', 'lives']

    def enter(self):
        self.timer = 350

    def update(self, dt=None, events=None):
        if self.timer > 0:
            self.game.level.update(dt)
            self.timer -= dt * 100
        else:
            self.game.state_machine.change_state("play")

    def handle_input(self, dt=None, events=None):
        pass

    def draw(self):
        self.game.screen.draw(self.bg_image, self.draw_flags)
        s = pygame.Surface((500, 500))
        s.set_alpha(190)
        s.fill((40, 40, 40))
        self.game.screen.surface.blit(s, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 250))
        if self.timer > 300:
            string = "READY?"
            string_width = self.game.screen.font_md.size(string)[0]
            string_height = self.game.screen.font_md.size(string)[1]
            text = pygame.font.Font.render(self.game.screen.font_md, string, True, (255, 255, 255))
            self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2))
        elif self.timer < 300 and self.timer > 0:
            string = str(int(self.timer // 100) + 1)
            string_width = self.game.screen.font_lg.size(string)[0]
            string_height = self.game.screen.font_lg.size(string)[1]
            text = pygame.font.Font.render(self.game.screen.font_lg, string, True, (255, 255, 255))
            self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2))

    def exit(self):
        pass