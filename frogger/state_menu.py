import pygame
from state_play import StatePlay
from state_game import StateGame
from utils import get_bg_image
from events import event_dispatcher

class StateMenu(StateGame):
    def __init__(self, game):
        self.game = game
        self.frog = game.frog
        self.screen = game.screen
        self.bg_image = get_bg_image("assets/menu_bg.png")
        self.play_buttons_beg = pygame.Rect(60, 540, 218, 70)
        self.play_buttons_adv = pygame.Rect(475, 540, 218, 70)

    def enter(self):
        pass

    def update(self, dt, events):
        for event in events: #look at all events
            if event.type == pygame.MOUSEMOTION:
                self.handle_input()

    def handle_input(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1:
            if self.play_buttons_beg.collidepoint(pos):
                self.game.state_machine.change_state(StatePlay(self.game))
            elif self.play_buttons_adv.collidepoint(pos):
                print("clicked - advanced")

    def draw(self):
        self.screen.surface.blit(self.bg_image, (0, 0))
        pygame.display.flip()

    def exit(self):
        pass