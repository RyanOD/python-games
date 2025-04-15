import pygame
from game import Game
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()
    # create game loop
    while not game.game_over():
        TimeManager.update(clock)
        # capture event keyboard events and either quit game of pass to InputHandler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            elif game.frog.alive:
                game.input_handler.handle_event(event)
                game.points()
        game.update()
        game.draw()

if __name__ == "__main__":
    main()