import pygame
from landscape_data import LANDINGS, VERTICES

class StatePlay:
    def __init__(self, game):
        self.game = game

    def enter(self):
        pass

    def handle_input(self):
        pass

    def update(self, dt, events):
        pass

    def draw(self):
        self.game.screen.draw_stars()
        self.game.screen.surface.blit(self.game.ship.image, (self.game.ship.x, self.game.ship.y))
        # draw terrain polygon with no border and filled with black to cover starfield background
        pygame.draw.polygon(self.game.screen.surface, (0, 0, 0), self.game.landscape.vertices, 0)
        # draw terrain polygon with white border and no fill
        pygame.draw.polygon(self.game.screen.surface, (194, 194, 194), self.game.landscape.vertices, 2)
        # draw each landing location in white with double thickness
        for landing in LANDINGS:
            pygame.draw.line(self.game.screen.surface, (255, 255, 255), landing[0], landing[1], 4)
    
    def exit(self):
        pass