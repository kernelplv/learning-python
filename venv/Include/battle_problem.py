from itertools import repeat as R

class Warrior:
    hp = 50
    power = 5

    is_alive = False

    def __init__(self):
        self.is_alive = True

    def isalive(self):
        if self.hp > 0:
            self.is_alive = True
            return True
        else:
            self.is_alive = False
            return False

    def damadged(self, unit):
        if unit.isalive():
            self.hp -= unit.power

    pass


class Knight(Warrior):
    power = Warrior.power + 2
    pass

class Army:

    def __init__(self):
        self.team = []

    def add_units(self, unit: Warrior, count: int ):
        for _ in R(None, count):
                self.team.append(unit())

    def comon(self)-> Warrior:
        return self.team.pop()

    def gohome(self, unit: Warrior):
        self.team.append(unit)

    def is_alive(self)-> bool:
        if len(self.team) > 0:
            return True
        return False
    pass

def fight(unit_1: Warrior, unit_2: Warrior):
    round = 1

    while unit_1.isalive() and unit_2.isalive():
        print(f'Round: {round} {unit_1.__class__.__name__}({unit_1.hp}) vs {unit_2.__class__.__name__}({unit_2.hp})')
        unit_2.damadged(unit_1)
        unit_1.damadged(unit_2)
        round += 1
    else:
        winner = unit_1.__class__.__name__ if not unit_2.isalive() else unit_2.__class__.__name__
        print(f'Winner *** {winner} ***')
    return unit_1.isalive()

class Battle:

    def fight(self, Ateam: Army, Bteam: Army):
        while Ateam.team and Bteam.team:
            a = Ateam.comon()
            b = Bteam.comon()
            if fight(a,b):
                Ateam.gohome(a)
            else:
                Bteam.gohome(b)
        return Ateam.is_alive()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    print(army_3.team)
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")