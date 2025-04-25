import pygame
from state_game import StateGame
from state_clear import StateClear
from events import event_dispatcher

class StatePlay(StateGame):
    def __init__(self, game):
        self.game = game
        self.frog = game.frog
        self.screen = game.screen

        event_dispatcher.dispatch('play_sound', 'main_theme')

    def enter(self):
        pass

    def update(self, dt, events):
        # delegate frog/object collision management to CollisionHandler class
        self.game.collision_handler.check_collisions(self.frog, self.game.level.objects)

        # delegate frog passive management to Frog class
        self.game.level.update(dt)

        # delegate scoring display management to Scoring class
        self.game.scoring.update()

        # delegate frog passive management to Frog class
        self.frog.update()

        # delegate frog active movement to Frog class 
        self.frog.move(dt)

        # update frog life status based on screen boundary collision
        if self.frog.alive and not self.screen.on_screen(self.frog):
            self.frog.die()

        # check to see if frog makes it to home goal location
        self.home_check()

        if not self.frog.alive and self.frog.dying_animation():
            self.reset_level()

    def draw(self):
        # clear the screen
        self.screen.reset()

        #draw timer

        # draw all objects (vehicles, logs, turtles) based on level_map data file
        for object in self.game.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))
        
        # if frog image is valid, draw frog image on the screen at frog.rect x, y position
        if self.frog.image:
            self.screen.surface.blit(self.frog.image, (self.frog.rect.x, self.frog.rect.y))

        # draw small frog image below starting row for each frog live left
        for f in range(0, self.frog.lives):
            self.screen.surface.blit(self.frog.menu_image, (f * 60 + 10, 850 + self.screen.lane_padding))

        # draw happy frog image in every home position that player has successfully reached
        level_cleared = True
        for home in self.game.homes:
            if home['occupied']:
                self.screen.surface.blit(self.frog.image_home, (((home['xl'] + home['xr']) // 2 - self.frog.image_home.get_width() // 2), 104))
            else:
                level_cleared = False

        if level_cleared:
            self.game.state_machine.change_state(StateClear)

        # draw player display
        self.screen.score(self.game.scoring.score)

        # flip the screen to display all of the above
        pygame.display.flip()

    # check if frog y position is within home (goal) row
    def frog_in_home_row(self):
        return self.frog.rect.top < 150

    # check if frog rect is in the goal home row and if so, update home occupied state to True and reset level
    def home_check(self):
        for home in self.game.homes:
            if self.frog.rect.centerx in range(home['xl'], home['xr']) and self.frog_in_home_row():
                home['occupied'] = True
                self.reset_level()

    # reset visited state of all rows to False then reset frog
    def reset_level(self):
        for row in self.game.scoring.rows:
            row['visited'] = False
        self.frog.reset()
    
    # end game if all frog lives lost
    def game_over(self):
        return self.lives == 0