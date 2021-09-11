from __future__ import annotations
from dataclasses import dataclass
import random


@dataclass
class Pokemon:
    name: str
    attack: Attack

    def perform_attack(self):
        if random.randrange(0, 100) <= self.attack.accuracy:
            print(f"{self.name} used {self.attack.name}!")
        else:
            print(f"{self.name}'s {self.attack.name} attack missed!")


@dataclass
class Attack:
    name: str
    battle_type: str
    base_power: int
    accuracy: int


class Thunderbolt(Attack):
    def __init__(self):
        super().__init__("Thunderbolt", "Electronic", 85, 90)


@dataclass
class BattleClass:
    attack_pokemon: Pokemon

    def perform_attack(self):
        self.attack_pokemon.perform_attack()


if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", Thunderbolt())
    battle = BattleClass(pikachu)
    battle.perform_attack()
