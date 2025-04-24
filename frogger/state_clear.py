class StateClear:
    def __init__(self, game):
        self.game = game

    def enter(self):
        pass

    def update(self, dt, events):
        # update x-position of all game objects (vehicles, logs, turtles, etc.)
        for object in self.game.level.objects:
            if not self.game.screen.on_screen(object):
                object.reset(self.game.screen)
            object.update(dt)

    def handle_input(self):
        pass

    def draw(self):
        # draw all objects (vehicles, logs, turtles) based on level_map data file
        for object in self.game.level.objects:
            if object.image:
                self.screen.surface.blit(object.image, (object.rect.x, object.rect.y))

        # draw small frog image below starting row for each frog live left
        for f in range(0, self.frog.lives):
            self.screen.surface.blit(self.frog.menu_image, (f * 60 + 10, 850 + self.screen.lane_padding))

        # draw happy frog image in every home position that player has successfully reached
        for home in self.game.homes:
            if home['occupied']:
                self.screen.surface.blit(self.frog.image_home, (((home['xl'] + home['xr']) // 2 - self.frog.image_home.get_width() // 2), 104))
        
        # draw player display
        self.screen.score(self.game.scoring.score)

    def exit(self):
        pass