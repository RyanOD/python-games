import pygame
from game import Game
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()

    # create game loop and run as long as player has frog lives remaining
    while game.frog.lives:
        TimeManager.update(clock)

        # update game
        game.update(TimeManager.get_delta_time())

        # draw game assets
        game.handle_input()

        # draw game assets
        game.draw()

if __name__ == "__main__":
    main()