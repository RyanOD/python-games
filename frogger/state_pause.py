import pygame
from state_game import StateGame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class StatePause(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()
        self.draw_flags = ['background', 'objects', 'frog', 'scoring', 'countdown', 'level', 'lives']

    def enter(self):
        pass

    def update(self, dt=None, events=None):
        pass

    def handle_input(self, dt=None, events=None):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.input_handler.handle_event(event, self.game, dt)

    def draw(self):
        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

        self.game.screen.draw(self.bg_image, self.draw_flags)
        s = pygame.Surface((500, 500))
        s.set_alpha(190)
        s.fill((40, 40, 40))
        self.game.screen.surface.blit(s, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 250))

        string = "PAUSED"
        string_width = self.game.screen.font_md.size(string)[0]
        string_height = self.game.screen.font_md.size(string)[1]
        text = pygame.font.Font.render(self.game.screen.font_md, string, True, (255, 255, 255))
        self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2))

    def exit(self):
        pass