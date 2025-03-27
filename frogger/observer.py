# Observable base class
class Observable:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observers(self, observer):
        self.observers.remove(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

# Observer base class
class Observer:
    def update(self, *args, **kwargs):
        pass