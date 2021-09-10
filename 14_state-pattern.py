from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class PokemonSettings:
    _pokemon_obj: Pokemon
    _nickname: str
    _level: int = 1

    @property
    def nickname(self):
        return self._nickname

    @property
    def level(self):
        return self._level

    @property
    def pokemon_obj(self):
        return self._pokemon_obj

    @pokemon_obj.setter
    def pokemon_obj(self, pokemon_obj):
        self._pokemon_obj = pokemon_obj

    @level.setter
    def level(self, level):
        self._level = level

        if isinstance(self.pokemon_obj.evolve_level, int):
            if self.pokemon_obj.evolve_level >= self.level:
                self.pokemon_obj = self.pokemon_obj.next_evolve_pokemon
                print(f"\nYour {self.nickname} is evolving into {self.pokemon_obj.name}!")

    @classmethod
    def create(cls, pokemon_obj, nickname, level):
        return cls(_pokemon_obj=pokemon_obj, _nickname=nickname, _level=level)

    def __str__(self):
        return f"""\npokemon: {self.pokemon_obj.name} \
         \nindex: {self.pokemon_obj.index} \
         \nnickname: {self.nickname}
         """


@dataclass
class Pokemon:
    index: int
    evolve_level: Optional[int]
    name: str


class Chikorita(Pokemon):
    def __init__(self):
        super().__init__(index=152, evolve_level=16, name="Chikorita")
        self.next_evolve_pokemon = Bayleef()


class Bayleef(Pokemon):
    def __init__(self):
        super().__init__(index=153, evolve_level=32, name="Bayleef")
        self.next_evolve_pokemon = Meganium()


class Meganium(Pokemon):
    def __init__(self):
        super().__init__(index=154, evolve_level=None, name="Meganium")
        self.next_evolve_pokemon = None


if __name__ == "__main__":
    chiko = PokemonSettings.create(pokemon_obj=Chikorita(), nickname="chiko", level=5)
    print(chiko)

    # Level Up and evolve
    chiko.level = 16
    print(chiko)

    # Level Up and evolve
    chiko.level = 32
    print(chiko)

    # Level Up without evolve
    chiko.level = 50
    print(chiko)
