from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Pokemon(metaclass=ABCMeta):
    index: int
    name: str

    def method(self):
        print(f"{self.name} has been called!")


class Iterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        pass

    @staticmethod
    @abstractmethod
    def next():
        pass


@dataclass
class PokemonIterator(Iterator):
    aggregates: list
    index: int = 0

    def has_next(self):
        return self.index < len(self.aggregates)

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("End of Iterator")


if __name__ == "__main__":
    bulbasaur = Pokemon(1, "bulbasaur")
    charmander = Pokemon(2, "charmander")
    squirtle = Pokemon(3, "squirtle")

    pokemon_aggregates = [bulbasaur, charmander, squirtle]
    iterable = PokemonIterator(pokemon_aggregates)

    while iterable.has_next():
        iterable.next().method()
