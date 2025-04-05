import pygame
from game import Game
from frog import Frog
from level import Level
from objects import Object
from sound import SoundHandler
from collision import CollisionHandler
from input import InputHandler
from commands import MoveUpCommand, MoveDownCommand
from events import event_dispatcher
from maps import *
from asset_paths import *
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()
    while not game.game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.lives = 0
            elif game.frog.alive:
                game.input_handler.handle_event(event)
        game.update()
        game.draw()
        TimeManager.update(clock)

if __name__ == "__main__":
    main()