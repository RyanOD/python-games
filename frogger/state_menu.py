import pygame
from state_game import StateGame
from utils import get_bg_image
from events import event_dispatcher
from config import SCREEN_WIDTH

class StateMenu(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = get_bg_image("assets/menu_bg.png")
        self.draw_flags = ['background']

        # state specific attributes beyond background
        self.play_button = pygame.Rect(268, 600, 218, 59)
        self.frog_img_1 = pygame.image.load('assets/frog_home_1.png')

    def enter(self):
        self.coin_dropped=False
        self.coin_drop_timer = 0

    def update(self, dt=None, events=None):
        if self.coin_dropped:
            if 0 < self.coin_drop_timer < 200:
                self.coin_drop_timer += 1
            else:
                self.game.state_machine.change_state("welcome")

    def draw(self):
        self.game.screen.draw(self.bg_image, self.draw_flags)
        self.game.screen.surface.blit(self.frog_img_1, (SCREEN_WIDTH // 2 - 30, 500))

    def handle_input(self, dt=None, events=None):
        for event in events:
            if pygame.mouse.get_pressed()[0] == 1:
                if self.play_button.collidepoint(pygame.mouse.get_pos()) and self.coin_dropped == False:
                    event_dispatcher.dispatch('play_sound', 'insert_coin')
                    self.frog_img_1 = pygame.image.load('assets/frog_home_2.png')
                    self.coin_dropped = True
                    self.coin_drop_timer += 1

    def exit(self):
        event_dispatcher.dispatch('stop_sound', 'insert_coin')