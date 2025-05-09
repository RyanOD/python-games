# Responsibility: Should handle input, because input behavior varies between states (e.g., Title screen vs. Game vs. Pause).

class StateMachine():
    def __init__(self, game):
        self.game = game
        self.current_state = None
        self.state_registry = {}
    
    def register(self, key, state_class):
        self.state_registry[key] = state_class
        
    def change_state(self, key):
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