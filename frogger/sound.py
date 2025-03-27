
import pygame
from events import event_dispatcher

class SoundHandler:
    def __init__(self):
        self.mixer = pygame.mixer.init()
        self.sounds = {
            'hop': pygame.mixer.Sound('assets/hop.mp3'),
            'die_road': pygame.mixer.Sound('assets/die_road.mp3')
        }
        self.sound_commands = {
            'hop': PlayHopSoundCommand(self.handle_sound),
            'die_road': PlayRoadDeathSoundCommand(self.handle_sound),
        }
        for sound in self.sounds.values():
            sound.set_volume(0.5)

        event_dispatcher.register("play_sound", self.handle_sound)

    def handle_sound(self, sound):
        if(sound in self.sounds):
            self.sounds[sound].play()

class PlayHopSoundCommand:
    def __init__(self, sound_handler):
        self.sound_handler = sound_handler

    def execute(self):
        self.sound_handler.handle_sound('hop')

class PlayRoadDeathSoundCommand:
    def __init__(self, sound_handler):
        self.sound_handler = sound_handler

    def execute(self):
        self.sound_handler.handle_sound('die_road')