import pygame
from events import event_dispatcher
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from state_game import StateGame

class StateGameOver(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()
        self.draw_flags = ['background', 'objects', 'frog', 'countdown']

        # state specific attributes beyond background
        self.play_button = pygame.Rect(SCREEN_WIDTH // 2 - 120, 455, 218, 70)
        
    def enter(self):
        event_dispatcher.dispatch('play_sound', 'game_over')

    def update(self, dt = None, events = None):
        # delegate frog passive management to Frog class
        self.game.level.update(dt)

    def handle_input(self, dt = None, events = None):
        for event in events:
            if pygame.mouse.get_pressed()[0] == 1:
                if self.play_button.collidepoint(pygame.mouse.get_pos()):
                    self.game.reset()
                    self.game.state_machine.change_state("play")

    def draw(self):
        self.game.screen.draw(self.bg_image, self.draw_flags)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

        s = pygame.Surface((500, 500))
        s.set_alpha(190)
        s.fill((40, 40, 40))
        self.game.screen.surface.blit(s, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 250))

        string = "GAME OVER"
        string_width = self.game.screen.font_md_sm.size(string)[0]
        string_height = self.game.screen.font_md_sm.size(string)[1]
        text = pygame.font.Font.render(self.game.screen.font_md_sm, string, True, (255, 255, 255))
        self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2 - 100))

        string = "SCORE = " + str(self.game.scoring.score)
        string_width = self.game.screen.font_sm.size(string)[0]
        string_height = self.game.screen.font_sm.size(string)[1]
        text = pygame.font.Font.render(self.game.screen.font_sm, string, True, (255, 255, 255))
        self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2 - 50))

        string = "PLAY AGAIN"
        string_width = self.game.screen.font_sm.size(string)[0]
        string_height = self.game.screen.font_sm.size(string)[1]
        text = pygame.font.Font.render(self.game.screen.font_sm, string, True, (255, 255, 255))
        self.game.screen.surface.blit(text, (SCREEN_WIDTH // 2 - string_width // 2, SCREEN_HEIGHT // 2 - string_height // 2 + 50))

    def exit(self):
        self.game.countdown.reset()
        self.game.frog.reset() # resets frog image, position, alive state, and death timer
        self.game.reset() # 
        self.game.scoring.score = 0
        for row in self.game.level.row_values:
            row['visited'] = False
        for home in self.game.homes:
            home['occupied'] = False
        
        event_dispatcher.dispatch('stop_sound', 'game_over')