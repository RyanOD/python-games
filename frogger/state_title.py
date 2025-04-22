import pygame
import webbrowser
from state_menu import StateMenu
from state_game import StateGame
from utils import get_bg_image
from events import event_dispatcher

class StateTitle(StateGame):
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.bg_image = get_bg_image("assets/title_bg.png")
        self.timer = 450
        event_dispatcher.dispatch('play_sound', 'title_theme')

    def enter(self):
        print("Entering title/menu state")

    def update(self, dt, events):
        pass

    def handle_input(self):
        pass

    def draw(self):
        if self.timer:
            self.screen.surface.blit(self.bg_image, (0, 0))
            pygame.display.flip()
            self.timer -= 1
        else:
            #webbrowser.open('https://www.nyt.com', new=2)
            self.game.state_machine.change_state(StateMenu(self.game))

    def exit(self):
        pass
        # end menu music