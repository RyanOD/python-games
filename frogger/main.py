import pygame
from game import Game
from classes import *

clock = pygame.time.Clock()
delta_time = clock.tick(60) / 1000

def main():
    game = Game()

    while not game.game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            game.input_handler.handle_event(event)

        game.update(delta_time)

        game.draw()

if __name__ == "__main__":
    main()