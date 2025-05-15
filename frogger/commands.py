# Responsibility: Define the behavior of user input
from state_play import StatePlay

class Command:
    def __init__(self):
        pass

    def execute(self, game, dt):
        pass

class MoveUpCommand(Command):
    def __init__(self):
        pass

    def execute(self, game, dt):
        game.frog.move(dt, "up")

class MoveRightCommand(Command):
    def __init__(self):
        pass

    def execute(self, game, dt):
        game.frog.move(dt, "right")

class MoveDownCommand(Command):
    def __init__(self):
        pass

    def execute(self, game, dt):
        game.frog.move(dt, "down")

class MoveLeftCommand(Command):
    def __init__(self):
        pass

    def execute(self, game, dt):
        game.frog.move(dt, "left")

class PauseGameCommand(Command):
    def __init__(self):
        pass

    def execute(self, game, dt):
        if isinstance(game.state_machine.current_state, StatePlay):
            game.state_machine.change_state("pause")
        else:
            game.state_machine.change_state("play")