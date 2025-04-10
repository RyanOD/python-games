import pygame
from events import event_dispatcher

class SoundHandler:
    def __init__(self):
        self.mixer = pygame.mixer.init()

        # dict of all game sound files
        self.sounds = {
            'hop': pygame.mixer.Sound('assets/hop.mp3'),
            'die_road': pygame.mixer.Sound('assets/die_road.mp3')
        }

        # set sound volumes
        for sound in self.sounds.values():
            sound.set_volume(0.5)

        # pass trigger word and method for playing sound to event_dispatcher which allows other modules to trigger sounds
        event_dispatcher.register("play_sound", self.handle_sound)

    # method registered with and called from event_dispatcher
    def handle_sound(self, sound):
        if(sound in self.sounds):
            self.sounds[sound].play()