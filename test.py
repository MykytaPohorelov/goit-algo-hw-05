"""Новий клас повинен бути Army і мати метод add_units() - для додавання вибраної кількості одиниць до армії. 
Перший доданий підрозділ буде першим, хто піде у бій, другий буде другим, ...
Також потрібно створити клас Battle() з функцією fight(), яка визначатиме найсильнішу армію.
Бої відбуваються за такими принципами:
спочатку відбувається двобій між першим воїном першої армії та першим воїном другої армії (використовується підрахунок FIFO). 
Як тільки один з них гине - в двобій вступає наступний воїн з армії, яка втратила бійця, а воїн, що вижив, продовжує битися з поточним здоров'ям. 
Так триває до тих пір, поки не загинуть всі солдати однієї з армій. У цьому випадку функція fight() має повернути True, якщо перша армія перемогла, або False, 
якщо друга була сильнішою.
Зверніть увагу, що армія 1 має перевагу починати кожен бій!"""

from collections import UserList
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Army(UserList):
    def add_units(self, unit_type, amount):
        for i in range(amount):
            self.append(unit_type())

    @property
    def is_exist(self):
        return bool(self.data)

class Battle():
    def fight(self, army_1: Army, army_2: Army):
        while army_2.is_exist and army_1.is_exist:
        
            if fight(army_1[0], army_2[0]):
                army_2.pop(0)
            else:
                army_1.pop(0)
        return army_1.is_exist
        


def fight(first_unit: Warrior, second_unit: Warrior)-> bool:
    while second_unit.is_alive and first_unit.is_alive:
        second_unit.health -= first_unit.attack
        if second_unit.is_alive:
            first_unit.health -= second_unit.attack

    return first_unit.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    battle.fight(army_1, army_2)

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")