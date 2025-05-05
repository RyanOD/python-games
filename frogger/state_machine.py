# Responsibility: Should handle input, because input behavior varies between states (e.g., Title screen vs. Game vs. Pause).

class StateMachine():
    def __init__(self):
        self.current_state = None
    
    def change_state(self, new_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def update(self, dt = None, events = None):
        if self.current_state:
            self.current_state.update(dt)

    def handle_input(self, dt, events):
        if self.current_state:
            self.current_state.handle_input(dt, events)

    def draw(self):
        if self.current_state:
            self.current_state.draw()