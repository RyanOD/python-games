import pygame
from game import Game
from classes import *

def main():
    game = Game()
    game.load_level(1)

    while not game.game_over():
        for object in game.objects:
            object.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            game.input_handler.handle_event(event)
        
        #game.input_handler.handle_input(pygame.key.get_pressed())

        game.draw()

if __name__ == "__main__":
    main()