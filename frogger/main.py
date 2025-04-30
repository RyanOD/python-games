import pygame
from game import Game
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()

    # create game loop and run as long as player has frog lives remaining
    while game.frog.lives > 0:
        TimeManager.update(clock)
        dt = TimeManager.get_delta_time()
        # update game
        game.update(dt)

        # draw game assets
        game.handle_input()

        # draw game assets
        game.draw()

        # flip the screen to display all of the above
        pygame.display.flip()

if __name__ == "__main__":
    main()