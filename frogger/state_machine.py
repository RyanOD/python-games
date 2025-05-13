# Responsibility: Should handle input, because input behavior varies between states (e.g., Title screen vs. Game vs. Pause).
from state_title import StateTitle
from state_menu import StateMenu
from state_play import StatePlay
from state_play import StatePlay
from state_clear import StateClear
from state_game_over import StateGameOver

class StateMachine():
    def __init__(self, game):
        self.game = game
        self.current_state = None
        self.state_registry = {}
        self.register("title", StateTitle)
        self.register("play", StatePlay)
        self.register("menu", StateMenu)
        self.register("clear", StateClear)
        self.register("game_over", StateGameOver)
    
    def register(self, key, state_class):
        self.state_registry[key] = state_class
        
    def change_state(self, key):
        if key not in self.state_registry:
            raise ValueError(f"State '{key}' not registered in state machine.")
        if self.current_state:
            self.current_state.exit()
        self.current_state = self.state_registry[key](self.game)
        self.current_state.enter()

    def update(self, dt = None, events = None):
        if self.current_state:
            self.current_state.update(dt)

    def handle_input(self, dt = None, events = None):
        if self.current_state:
            self.current_state.handle_input(dt, events)

    def draw(self):
        if self.current_state:
            self.current_state.draw()