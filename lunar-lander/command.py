import pygame

class Command:
    def execute(self):
        pass

class AccelerateCommand:
    def __init__(self, ship):
        self.ship = ship
    
    def execute(self):
        self.ship.update("accelerate")
    
class RotateCWCommand:
    def __init__(self, ship):
        self.ship = ship
    
    def execute(self):
        self.ship.update("rotate_cw")

class RotateCCWCommand:
    def __init__(self, ship):
        self.ship = ship
    
    def execute(self):
        self.ship.update("rotate_ccw")