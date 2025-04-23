import pygame
from game import Game
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()
    while not game.game_over():
        TimeManager.update(clock)
        game.update((TimeManager.get_delta_time()))
        game.handle_input()
        game.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()