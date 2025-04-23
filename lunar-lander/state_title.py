import pygame
from state_game import StateGame
from state_play import StatePlay

class StateTitle(StateGame):
    def __init__(self, game):
        self.game = game
        self.bg_image = pygame.transform.scale(pygame.image.load('images/title_bg.png'), (game.screen.width, game.screen.height))
    
    def enter(self):
        pass

    def update(self, dt, events):
        pass

    def handle_input(self):
        if pygame.mouse.get_pressed()[0] == 1:
            self.game.state_machine.change_state(StatePlay(self.game))

    def draw(self):
        self.game.screen.draw_stars()
        self.game.screen.surface.blit(self.bg_image, (0, 0))

    def exit(self):
        pass