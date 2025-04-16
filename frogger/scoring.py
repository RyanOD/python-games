import pygame

class Scoring:
    def __init__(self, frog):
        self.score = 0
        self.scoring = [
            {"visited": False, "value": 0},
            {"visited": False, "value": 100},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 10},
            {"visited": False, "value": 0},
            {"visited": False, "value": 0},
        ]
        self.frog = frog
    
    def update(self):
        row = self.scoring[self.frog.rect.y // 50 - 1]
        if not row["visited"]:
            self.score += row["value"]
            row["visited"] = True