import math
import random
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Damage:
    _type: str
    _power: int

    @property
    def power(self):
        return self._power

    @property
    def type(self):
        return self._type


@dataclass
class Pokemon(metaclass=ABCMeta):
    id: int
    name: str
    type: str
    power: int
    defense: int

    @abstractmethod
    def calculate_damage_multiplier(self):
        pass

    def calculate_damage(self):
        self.damage_multiplier = self.calculate_damage_multiplier()
        self.damage = int(self.calculate_damage_impact())

    def show_damage(self):
        print(f"{self.name} damage is:", self.damage)

    def get_damage(self, damage_obj: Damage):
        print(f"Got {damage_obj.type} damange!")
        self.damage_obj = damage_obj

    def calculate_damage_impact(self):
        return (
            (self.damage_multiplier * self.damage_obj.power)
            - math.floor(self.defense * self.damage_multiplier)
            + 1
        )

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, type: {self.type}, power: {self.power}, defense: {self.defense}"


class GrassPokemon(Pokemon):
    def __init__(self, id, name, power, defense):
        super().__init__(id=id, name=name, type='Grass', power=power, defense=defense)

    def calculate_damage_multiplier(self):
        multiple = 1

        if random.randrange(0, 100) <= 15:
            print("Critical Hit!")
            multiple *= 2

        if self.damage_obj.type == "Water":
            print("It was not very effective!")
            multiple /= 2

        return multiple


class FirePokemon(Pokemon):
    def __init__(self, id, name, power, defense):
        super().__init__(id=id, name=name, type='Fire', power=power, defense=defense)

    def calculate_damage_multiplier(self):
        multiple = 1

        if random.randrange(0, 100) <= 15:
            print("Critical Hit!")
            multiple *= 2

        if self.damage_obj.type == "Water":
            print("It was very effective!")
            multiple *= 2

        return multiple


class IcePokemon(Pokemon):
    def __init__(self, id, name, power, defense):
        super().__init__(id=id, name=name, type='Ice', power=power, defense=defense)

    def calculate_damage_multiplier(self):
        multiple = 1

        if random.randrange(0, 100) <= 15:
            print("Critical Hit!")
            multiple *= 2

        if self.damage_obj.type == "Water":
            print("It was not very effective!")
            multiple /= 2

        return multiple


water_type_damage = Damage("Water", 70)

chikorita = GrassPokemon(id=152, name="치코리타", power=70, defense=70)
charmander = FirePokemon(id=4, name="파이리", power=75, defense=60)
glaceon = IcePokemon(id=471, name="글레이시아", power=70, defense=55)

print()
print(chikorita)
chikorita.get_damage(water_type_damage)
chikorita.calculate_damage()
chikorita.show_damage()

print()
print(charmander)
charmander.get_damage(water_type_damage)
charmander.calculate_damage()
charmander.show_damage()

print()
print(glaceon)
glaceon.get_damage(water_type_damage)
glaceon.calculate_damage()
glaceon.show_damage()
