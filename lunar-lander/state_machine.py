class StateMachine:
    def __init__(self):
        self.current_state = None
    
    def change_state(self, state):
        self.current_state = state
    
    def update(self, dt, events):
        if self.current_state:
            self.current_state.update(dt, events)

    def handle_input(self):
        if self.current_state:
            self.current_state.handle_input()

    def draw(self):
        if self.current_state:
            self.current_state.draw()