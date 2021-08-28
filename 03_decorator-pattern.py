from abc import ABCMeta, abstractmethod


class Pokemon(metaclass=ABCMeta):
    def __init__(self):
        self._description = "None"

    @property
    def description(self):
        return self._description

    @property
    @abstractmethod
    def rare_value(self):
        pass


class CondimentDecorator(Pokemon, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def description(self):
        pass
        
    @property
    @abstractmethod
    def rare_value(self):
        pass


class Pikachu(Pokemon):
    def __init__(self):
        self._description = "Pikachu!"

    @property
    def rare_value(self):
        return 150


class Squirtle(Pokemon):
    def __init__(self):
        self._description = "Squirtle!"

    @property
    def rare_value(self):
        return 100


class Golden(CondimentDecorator):
    def __init__(self, poke):
        super().__init__()
        self.pokemon = poke

    @property
    def description(self):
        return self.pokemon.description + "Golden "

    @property
    def rare_value(self):
        return self.pokemon.rare_value + 2000


class Super(CondimentDecorator):
    def __init__(self, poke):
        super().__init__()
        self.pokemon = poke

    @property
    def description(self):
        return self.pokemon.description + "Super "

    @property
    def rare_value(self):
        return self.pokemon.rare_value + 2000


pikachu = Pikachu()
squirtle = Squirtle()

golden_pikachu = Golden(pikachu)
golden_squirtle = Golden(squirtle)

super_golden_pikachu = Super(Golden(pikachu))
super_golden_squirtle = Super(Golden(squirtle))


print("Pikachu description:", pikachu.description)
print("Pikachu rare value:", pikachu.rare_value)
print()

print("Golden Pikachu description:", golden_pikachu.description)
print("Golden Pikachu rare value:", golden_pikachu.rare_value)
print()

print("Super Golden Pikachu description:", super_golden_pikachu.description)
print("Super Golden Pikachu rare value:", super_golden_pikachu.rare_value)

#####

print()
print()

#####

print("Squirtle description:", squirtle.description)
print("Squirtle rare value:", squirtle.rare_value)
print()

print("Golden Squirtle description:", golden_squirtle.description)
print("Golden Squirtle rare value:", golden_squirtle.rare_value)
print()

print("Super Golden Squirtle description:", super_golden_squirtle.description)
print("Super Golden Squirtle rare value:", super_golden_squirtle.rare_value)
