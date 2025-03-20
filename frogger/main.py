import pygame
from game import Game
from classes import *

def main():
    game = Game()
    game.level.load_level(1)

    while not game.game_over():
        for object in game.level.objects:
            object.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            game.input_handler.handle_event(event)

        game.update()
        game.draw()

if __name__ == "__main__":
    main()