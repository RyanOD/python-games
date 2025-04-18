import pygame
from game import Game
from time_manager import TimeManager

clock = pygame.time.Clock()

def main():
    game = Game()
    # create game loop and run as long as player has frog lives remaining

    while game.frog.lives:
        TimeManager.update(clock)

        # capture keyboard events and either quit game or pass to InputHandler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.frog.lives = 0
            elif game.frog.alive:
                game.input_handler.handle_event(event)
        
        # update game
        game.update()

if __name__ == "__main__":
    main()