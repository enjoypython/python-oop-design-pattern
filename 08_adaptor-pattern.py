from abc import ABCMeta, abstractmethod
from typing import Any


class Pokemon(metaclass=ABCMeta):
    @property
    @abstractmethod
    def cry(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Pikachu(Pokemon):
    def __init__(self) -> None:
        self._name = "Pikachu"

    @property
    def cry(self):
        return "Pikachu!"

    def electro_attack(self):
        return "10만 볼트!"

    @property
    def name(self):
        return self._name


class Eevee:
    def __init__(self) -> None:
        self._name = "Eevee"

    @property
    def cry(self):
        return "Eevee!"

    def normal_attack(self):
        return "몸통박치기!"

    @property
    def name(self):
        return self._name


class PokemonAdapter:
    def __init__(self, obj, **adapted_methods) -> None:
        self._obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._obj, attr)

    @property
    def cry(self):
        return self._obj.cry


if __name__ == "__main__":
    pokemon_objects = list()

    pikachu = Pikachu()
    pokemon_objects.append(PokemonAdapter(pikachu, attack=pikachu.electro_attack()))

    eevee = Eevee()
    pokemon_objects.append(PokemonAdapter(eevee, attack=eevee.normal_attack()))

    for obj in pokemon_objects:
        print(f"가라 {obj.name}! : {obj.cry}")
        print(obj.attack)
        print()
