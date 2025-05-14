import pygame
from events import event_dispatcher
from config import SCREEN_WIDTH
from state_game import StateGame

class StateGameOver(StateGame):
    def __init__(self, game):
        super().__init__(game)
        self.bg_image = pygame.image.load("assets/bg.png").convert()

        # state specific attributes beyond background
        self.play_button = pygame.Rect(SCREEN_WIDTH // 2 - 120, 805, 218, 70)
        
    def enter(self):
        event_dispatcher.dispatch('play_sound', 'game_over')

    def update(self, dt = None, events = None):
        # delegate frog passive management to Frog class
        self.game.level.update(dt)

    def handle_input(self, dt = None, events = None):
        for event in events: #look at all events
            if event.type == pygame.QUIT:
                self.game.frog.lives = 0
            elif pygame.mouse.get_pressed()[0] == 1:
                if self.play_button.collidepoint(pygame.mouse.get_pos()):
                    from state_menu import StateMenu
                    self.game.reset()
                    self.game.state_machine.change_state("menu")

    def draw(self):
        # clear the screen
        self.game.screen.draw(self.bg_image, self.game.level.objects, self.game.frog, self.game.scoring, self.game.countdown)

        # draw happy frog image in every home position that player has successfully reached
        for col, home in enumerate(self.game.homes):
            if home['occupied']:
                self.game.screen.surface.blit(self.game.frog.image_home, (col * 150 + 75 - 20, 104))

        pygame.draw.rect(self.game.screen.surface, (10, 10, 10), (SCREEN_WIDTH // 2 - 150, 405, 300, 40))
        font = pygame.font.Font("assets/upheavtt.ttf", 34)
        game_over_text = pygame.font.Font.render(font, "Game Over", True, (255, 255, 255))
        self.game.screen.surface.blit(game_over_text, (SCREEN_WIDTH // 2 - 84, 407))

        pygame.draw.rect(self.game.screen.surface, (10, 10, 10), (SCREEN_WIDTH // 2 - 130, 805, 260, 40))
        game_over_text = pygame.font.Font.render(font, "Play Again", True, (255, 255, 255))
        self.game.screen.surface.blit(game_over_text, (SCREEN_WIDTH // 2 - 99, 807))

    def exit(self):
        event_dispatcher.dispatch('stop_sound', 'game_over')