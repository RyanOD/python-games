import pygame
from state_play import StatePlay
from state_game import StateGame
from utils import get_bg_image, get_image
from events import event_dispatcher
from config import SCREEN_WIDTH

class StateMenu(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = get_bg_image("assets/menu_bg.png")
        self.play_buttons_beg = pygame.Rect(60, 540, 218, 70)
        self.play_buttons_adv = pygame.Rect(475, 540, 218, 70)
        self.rc_link = pygame.Rect(255, 710, 245, 15)
        self.gh_link = pygame.Rect(260, 745, 234, 15)
        self.coin_drop_timer = 0
        self.coin_dropped = False
        self.frog_img_1 = pygame.image.load('assets/frog_home_1.png')

    def enter(self):
        pass

    def update(self, dt = None, events = None):
        if self.coin_dropped:
            if 0 < self.coin_drop_timer < 200:
                self.coin_drop_timer += 1
            else:
                self.game.state_machine.change_state(StatePlay(self.game))

    def draw(self):
        self.game.screen.draw(self.bg_image)
        self.game.screen.surface.blit(self.frog_img_1, (SCREEN_WIDTH // 2 - 30, 545))

    def handle_input(self, dt, events):
        for event in events: #look at all events
            if event.type == pygame.QUIT:
                self.frog.lives = 0
            elif pygame.mouse.get_pressed()[0] == 1:
                if self.play_buttons_beg.collidepoint(pygame.mouse.get_pos()) and self.coin_dropped == False:
                    event_dispatcher.dispatch('play_sound', 'insert_coin')
                    self.frog_img_1 = pygame.image.load('assets/frog_home_2.png')
                    self.coin_dropped = True
                    self.coin_drop_timer += 1
                elif self.play_buttons_adv.collidepoint(pygame.mouse.get_pos()) and self.coin_dropped == False:
                    print("clicked - advanced")

    def exit(self):
        pass