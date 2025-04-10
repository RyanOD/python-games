# Responsibility: Registers  for observer pattern being used to manage game sounds

class EventDispatcher:
    # create empty dict of listeners
    def __init__(self):
        self.listeners = {}
    
    # create an array for each new event_type dict (event_type: listener function) and append to self.listeners
    def register(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    # call listener
    def dispatch(self, event_type, *args, **kwargs):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(*args, **kwargs)

# Global event dispatcher
event_dispatcher = EventDispatcher()