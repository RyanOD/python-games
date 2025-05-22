class TimeManager:
    delta_time = 0.0

    # update delta_time with seconds (milliseconds / 1000) since last frame 
    @classmethod
    def update(cls, clock):
        cls.delta_time = clock.tick(60) / 1000

    # return delta_time (seconds since last frame)
    @classmethod
    def get_delta_time(cls):
        return cls.delta_time