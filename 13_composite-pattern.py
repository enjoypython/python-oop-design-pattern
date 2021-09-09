from dataclasses import dataclass, field


@dataclass
class Pokedex:
    _dex_name: str = "Pokedex"
    _children: list = field(default_factory=list)

    def print_data(self):
        for child in self._children:
            child.read_data()
        print(self._dex_name)

    def add(self, pokemon_data):
        self._children.append(pokemon_data)


@dataclass
class PokemonData:
    _index: int
    _name: str

    def read_data(self):
        print("index:", self._index, "name:", self._name)


def main():
    pokedex = Pokedex()

    pikachu = PokemonData(25, "pikachu")
    eevee = PokemonData(132, "eevee")

    pokedex.add(pikachu)
    pokedex.add(eevee)

    pokedex.print_data()


if __name__ == "__main__":
    main()
