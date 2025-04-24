# Responsibility: Define the behavior of user input

class Command:
    def execute(self):
        pass

class MoveUpCommand:
    def __init__(self, frog, dt):
        self.frog = frog

    def execute(self, dt):
        self.frog.move(dt, "up")

class MoveRightCommand:
    def __init__(self, frog, dt):
        self.frog = frog

    def execute(self, dt):
        self.frog.move(dt, "right")

class MoveDownCommand:
    def __init__(self, frog, dt):
        self.frog = frog

    def execute(self, dt):
        self.frog.move(dt, "down")

class MoveLeftCommand:
    def __init__(self, frog, dt):
        self.frog = frog

    def execute(self, dt):
        self.frog.move(dt, "left")