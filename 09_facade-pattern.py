from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class LocalPokemonServer(Server):
    def boot(self):
        print("Local Network Server On")

    def shutdown(self):
        print("Local Network Server Off")


class GameNetworkServer(Server):
    def boot(self):
        print("Global Network Server On")

    def shutdown(self):
        print("Local Network Server Off")


class GlobalBattleServer(Server):
    def boot(self):
        print("GBS Server On")

    def shutdown(self):
        print("Local Network Server Off")


class GlobalTradeServer(Server):
    def boot(self):
        print("GTS Server On")

    def shutdown(self):
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
