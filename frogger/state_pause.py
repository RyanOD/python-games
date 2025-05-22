import pygame
from state_game import StateGame
from config import SCREEN_WIDTH

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
        self.game.screen.draw(self.bg_image, self.draw_flags)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))
        
        pygame.draw.rect(self.game.screen.surface, (10, 10, 10), (SCREEN_WIDTH // 2 - 100, 405, 200, 40))
        font = pygame.font.Font("assets/upheavtt.ttf", 34)
        text = pygame.font.Font.render(font, "GAME PAUSED", True, (255, 255, 255))
        self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - 100, 407))

    def exit(self):
        print('exiting paused state')