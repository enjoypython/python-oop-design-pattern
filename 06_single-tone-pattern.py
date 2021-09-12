from dataclasses import dataclass
import collections


class Singleton:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class Ball:
    def __init__(self, name, stock):
        self._name = name
        self._stock = stock

    @property
    def name(self):
        return self._name

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock

    def sale(self, amount) -> bool:
        if self.stock >= amount:
            self.stock -= amount
            return True
        else:
            # print("재고부족 주문실패")
            return False


class PokeBall(Ball):
    def __init__(self):
        super().__init__("PokeBall", 100)


class GreatBall(Ball):
    def __init__(self):
        super().__init__("GreatBall", 50)


class UltraBall(Ball):
    def __init__(self):
        super().__init__("UltraBall", 10)


class MasterBall(Ball):
    def __init__(self):
        super().__init__("MasterBall", 1)


class PokeballStore(Singleton):
    poke_ball = PokeBall()
    great_ball = GreatBall()
    ultra_ball = UltraBall()
    master_ball = MasterBall()

    @classmethod
    def purchase(cls, item: str, amount: int):
        response = None
        if item.lower() == "pokeball":
            response = cls.poke_ball.sale(amount)
        elif item.lower() == "greatball":
            response = cls.great_ball.sale(amount)
        elif item.lower() == "ultraball":
            response = cls.ultra_ball.sale(amount)
        elif item.lower() == "masterball":
            response = cls.master_ball.sale(amount)

        return response


class Trainer:
    def __init__(self, name):
        self._name = name
        self._items = collections.defaultdict(int)

    def buy_ball(self, item: str, amount: int):
        pokeball_store = PokeballStore()

        if response := pokeball_store.purchase(item, amount):
            self._items[item] += amount
            print(f"{self._name} bought {amount} amount(s) of {item}!")
        else:
            print(f"{self._name} could not buy {amount} amount(s) of {item}!")

    def show_items(self):
        print(self._items)


def main():
    trainer_01 = Trainer("지우")
    trainer_02 = Trainer("웅")
    trainer_03 = Trainer("로켓단")

    trainer_01.buy_ball("pokeball", 50)
    trainer_02.buy_ball("pokeball", 40)
    trainer_03.buy_ball("pokeball", 30)

    print()

    trainer_01.buy_ball("greatball", 30)
    trainer_02.buy_ball("greatball", 20)
    trainer_03.buy_ball("greatball", 10)

    print()

    trainer_01.buy_ball("masterball", 1)
    trainer_02.buy_ball("masterball", 1)
    trainer_03.buy_ball("masterball", 1)

    print()

    trainer_01.show_items()
    trainer_02.show_items()
    trainer_03.show_items()


if __name__ == "__main__":
    main()
