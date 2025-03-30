import pygame

class TimeManager:
    delta_time = 0.0

    @classmethod
    def update(cls, clock):
        cls.delta_time = clock.tick(60) / 1000

    @classmethod
    def get_delta_time(cls):
        return cls.delta_time