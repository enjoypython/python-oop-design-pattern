from abc import ABCMeta, abstractmethod


class Subject:
    def __init__(self):
        self._observer = []

    def attach(self, observer):
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            raise ValueError("Target Observer Not Found")


class Pokemon(Subject):
    def __init__(self, name, hp):
        super().__init__()
        self.name = name
        self.hp = hp
        self.status = "Health"

    def notify_observer(self):
        for observer in self._observer:
            observer.update(self.hp, self.status)

    def change_status(self, hp, status):
        self.hp = hp
        self.status = status
        self.notify_observer()


class EventObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def display(self):
        pass


class CurrentEventObserver(EventObserver):
    def update(self, hp, status):
        self.hp = hp
        self.status = status
        self.display()

    def display(self):
        print(f"Current Event Observer [hp : {self.hp}, status : {self.status}]")


class StaticEventObserver(EventObserver):
    def update(self, hp, status):
        self.hp = hp
        self.status = status
        self.display()

    def display(self):
        print(f"Static Event Observer [hp : {self.hp}, status : {self.status}]")


pikachu = Pokemon("pikachu", 100)

current_observer = CurrentEventObserver()
static_observer = StaticEventObserver()

pikachu.attach(current_observer)
pikachu.attach(static_observer)

pikachu.change_status("110", "Excellent")

print()

pikachu.change_status("90", "Good")
