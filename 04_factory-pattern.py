from abc import ABCMeta, abstractmethod


class Pokemon(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def paint(self):
        pass

    def __str__(self):
        return self.paint + " " + self.name


class Pikachu(Pokemon):
    @property
    def name(self):
        return "Pikachu"

    @property
    def paint(self):
        return "Yellow"


class Squirtle(Pokemon):
    @property
    def name(self):
        return "Squirtle"

    @property
    def paint(self):
        return "Blue"


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_pokemon(self, type):
        pass


class ElectronicPokemonFactory(Factory):
    def create_pokemon(self, type):
        if type == "Pikachu":
            print("Created", type, "Pokemon!")
            return Pikachu()


class WaterPokemonFactory(Factory):
    def create_pokemon(self, type):
        if type == "Squirtle":
            print("Created", type, "Pokemon!")
            return Squirtle()


if __name__ == "__main__":
    electro_pokemon_factory = ElectronicPokemonFactory()
    pikachu = electro_pokemon_factory.create_pokemon("Pikachu")
    print(pikachu)

    print()

    water_pokemon_factory = WaterPokemonFactory()
    squirtle = water_pokemon_factory.create_pokemon("Squirtle")
    print(squirtle)
