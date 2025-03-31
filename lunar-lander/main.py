import pygame
from game import Game
from ship import Ship
from screen import Screen
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()
    while not game.game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            elif game.ship.alive:
                game.input_handler.handle_event(event)
        game.update()
        game.draw()
        TimeManager.update(clock)
        pygame.display.flip()

if __name__ == "__main__":
    main()