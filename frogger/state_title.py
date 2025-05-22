from state_game import StateGame
from utils import get_bg_image
from events import event_dispatcher

class StateTitle(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = get_bg_image("assets/title_bg.png")
        self.draw_flags = ['background']
        
        # state specific attributes beyond background
        self.timer = 400

    def enter(self):
        event_dispatcher.dispatch('play_sound', 'title_theme')

    def update(self, dt=None, events=None):
        pass

    def handle_input(self, dt=None, events=None):
        pass

    def draw(self):
        if self.timer:
            self.game.screen.draw(self.bg_image, self.draw_flags)
            self.timer -= 1
        else:
            self.game.state_machine.change_state("menu")

    def exit(self):
        event_dispatcher.dispatch('stop_sound', 'title_theme')