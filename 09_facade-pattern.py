from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def boot(self):
        pass

    @staticmethod
    @abstractmethod
    def shutdown(self):
        pass


class LocalPokemonServer(Server):
    @staticmethod
    def boot():
        print("Local Network Server On")

    @staticmethod
    def shutdown():
        print("Local Network Server Off")


class GameNetworkServer(Server):
    @staticmethod
    def boot():
        print("Global Network Server On")

    @staticmethod
    def shutdown():
        print("Local Network Server Off")


class GlobalBattleServer(Server):
    @staticmethod
    def boot():
        print("GBS Server On")

    @staticmethod
    def shutdown():
        print("Local Network Server Off")


class GlobalTradeServer(Server):
    @staticmethod
    def boot():
        print("GTS Server On")

    @staticmethod
    def shutdown():
        print("Local Network Server Off")


class PokemonOperatingSystem:
    """The Facade"""

    def __init__(self):
        self.ls = LocalPokemonServer()
        self.ns = GameNetworkServer()
        self.bs = GlobalBattleServer()
        self.ts = GlobalTradeServer()

    def run_start(self):
        [i.boot() for i in (self.ls, self.ns, self.bs, self.ts)]

    def quit(self):
        [i.shutdown() for i in (self.ls, self.ns, self.bs, self.ts)]


def main():
    poke_os = PokemonOperatingSystem()
    poke_os.run_start()
    poke_os.quit()


if __name__ == "__main__":
    main()
