# Responsibility: Define the behavior of user input

class Command:
    def __init__(self, frog):
        self.frog = frog

    def execute(self, dt):
        pass

class MoveUpCommand(Command):
    def __init__(self, frog):
        super().__init__(frog)

    def execute(self, dt):
        self.frog.move(dt, "up")

class MoveRightCommand(Command):
    def __init__(self, frog):
        super().__init__(frog)

    def execute(self, dt):
        self.frog.move(dt, "right")

class MoveDownCommand(Command):
    def __init__(self, frog):
        super().__init__(frog)

    def execute(self, dt):
        self.frog.move(dt, "down")

class MoveLeftCommand(Command):
    def __init__(self, frog):
        super().__init__(frog)

    def execute(self, dt):
        self.frog.move(dt, "left")