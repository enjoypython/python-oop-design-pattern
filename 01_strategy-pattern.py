from abc import ABCMeta, abstractmethod


class Pokemon(metaclass=ABCMeta):
    def __init__(self):
        self.attack_behavior = None
        self.crying_behavior = None

    def perform_attack(self):
        self.attack_behavior.attack()

    def perform_crying(self):
        self.crying_behavior.crying()


class Pikachu(Pokemon):
    def __init__(self):
        self.attack_behavior = ElectronicAttack()
        self.crying_behavior = PikachuCrying()


class Squirtle(Pokemon):
    def __init__(self):
        self.attack_behavior = AquaAttack()
        self.crying_behavior = SquirtleCrying()


class AttackBehavior(metaclass=ABCMeta):
    
    @abstractmethod
    def attack(self):
        pass


class ElectronicAttack(AttackBehavior):
    def attack(self):
        print('100만 볼트!')


class AquaAttack(AttackBehavior):
    def attack(self):
        print('물대포!')


class CryingBehavior(metaclass=ABCMeta):
    
    @abstractmethod
    def crying(self):
        pass


class PikachuCrying(CryingBehavior):
    def crying(self):
        print('Pika Pika')


class SquirtleCrying(CryingBehavior):
    def crying(self):
        print('꼬북 꼬북')


# Pikachu
pikachu = Pikachu()
pikachu.perform_crying()
pikachu.perform_attack()

print()
print()

# Squirtle
squirtle = Squirtle()
squirtle.perform_crying()
squirtle.perform_attack()