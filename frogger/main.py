import pygame
from game import Game
from classes import *

def main():
    game = Game(1)

    while not game.game_over():
        delta_time = game.clock.tick(60) / 1000

        for lane in game.lanes:
            lane.update(delta_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            game.input_handler.handle_event(event, game.sound_handler)

        game.update()

        game.draw()

if __name__ == "__main__":
    main()