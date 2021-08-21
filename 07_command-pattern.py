from abc import ABCMeta, abstractmethod


# Invoker
class TrainerControl:
    def __init__(self):
        self.on_command  = []
        self.off_command = []

    def set_command(self, on_command):
        self.on_command.append(on_command)

    def on_shortcut_command(self, slot):
        self.on_command[slot].execute()


# Receiver
class Mode(metaclass=ABCMeta):
    @abstractmethod
    def on(self):
        pass

    def off(self):
        pass

class Attack(Mode):
    def on(self):
        print("Attack Mode On")

    def off(self):
        print("Attack Mode Off")

class Defense(Mode):
    def on(self):
        print('Defense Mode On')

    def off(self):
        print('Defense Mode Off')

class Hide(Mode):
    def on(self):
        print('Hide Mode On')

    def off(self):
        print('Hide Mode Off')


# Command
class Command(metaclass=ABCMeta):
    def __init__(self):
        self.status = False

    @abstractmethod
    def execute(self):
        pass


class AttackCommand(Command):
    def __init__(self, attack:Attack):
        self.attack = attack
        self.status = False

    def execute(self):
        if self.status is False:
            self.attack.on()
            self.status = True
        else:
            self.attack.off()
            self.status = False


class DefenseCommand(Command):
    def __init__(self, defense:Defense):
        self.defense = defense
        self.status = False

    def execute(self):
        if self.status is False:
            self.defense.on()
            self.status = True
        else:
            self.defense.off()
            self.status = False


class HideCommand(Command):
    def __init__(self, hide:Hide):
        self.hide = hide
        self.status = False

    def execute(self):
        if self.status is False:
            self.hide.on()
            self.status = True
        else:
            self.hide.off()
            self.status = False


# Invoker
ash = TrainerControl()

# Receiver
attack = Attack()
defense = Defense()
hide = Hide()

# Command
attack_toggle_command = AttackCommand(attack)
defense_toggle_command = DefenseCommand(defense)
hide_toggle_command = HideCommand(hide)

# SetCommand
ash.set_command(attack_toggle_command)
ash.set_command(defense_toggle_command)
ash.set_command(hide_toggle_command)

# Execute
ash.on_shortcut_command(0)
ash.on_shortcut_command(0)

ash.on_shortcut_command(1)
ash.on_shortcut_command(2)
ash.on_shortcut_command(2)
ash.on_shortcut_command(1)
