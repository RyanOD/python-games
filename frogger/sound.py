import pygame
from events import event_dispatcher

class SoundHandler:
    def __init__(self):
        self.mixer = pygame.mixer.init()

        # dict of all game sound files
        self.sounds = {
                'hop': {'mixer': pygame.mixer.Sound('assets/hop.mp3'), 'repeat': 0},
                'die': {'mixer': pygame.mixer.Sound('assets/die.mp3'), 'repeat': 0},
                'title_theme': {'mixer': pygame.mixer.Sound('assets/title_theme.mp3'), 'repeat': 0},
                'main_theme': {'mixer': pygame.mixer.Sound('assets/main_theme.mp3'), 'repeat': -1},
                'insert_coin': {'mixer': pygame.mixer.Sound('assets/insert_coin.mp3'), 'repeat': 0},
                'landing_safe': {'mixer': pygame.mixer.Sound('assets/landing_safe.mp3'), 'repeat': 0},
                'level_clear': {'mixer': pygame.mixer.Sound('assets/level_clear.mp3'), 'repeat': 0},
                'game_over': {'mixer': pygame.mixer.Sound('assets/game_over.mp3'), 'repeat': 0},
            }

        # set sound volumes
        for key, value in self.sounds.items():
            value['mixer'].set_volume(0.5)

        # pass trigger word and method for playing sound to event_dispatcher which allows other modules to trigger sounds
        event_dispatcher.register("play_sound", self.play_sound)
        event_dispatcher.register("stop_sound", self.stop_sound)

    # method registered with and called from event_dispatcher
    def play_sound(self, sound):
        self.sounds[sound]['mixer'].play(loops=self.sounds[sound]['repeat'])

    def stop_sound(self, sound):
        self.sounds[sound]['mixer'].stop()