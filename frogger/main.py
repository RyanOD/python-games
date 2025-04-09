import pygame
from game import Game
from time_manager import TimeManager


clock = pygame.time.Clock()

def main():
    game = Game()
    # create game loop
    while not game.game_over():
        # capture events and pass to InputHandler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            if game.frog.alive:
                game.input_handler.handle_event(event)
        game.update()
        game.draw()
        TimeManager.update(clock)

if __name__ == "__main__":
    main()