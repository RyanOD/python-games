# Responsibility: Define the behavior of user input

class Command:
    def execute(self):
        pass
'''
class QuitCommand:
    def __init__(self, frog):
        self.frog = frog
    
    def execute(self):
        self.frog.lives = 0
'''
class MoveUpCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("up")

class MoveRightCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("right")

class MoveDownCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("down")

class MoveLeftCommand:
    def __init__(self, frog):
        self.frog = frog

    def execute(self):
        self.frog.update("left")