import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
    def attack(self, enemy):
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.health -= self.power
        time.sleep(0.5)
    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))
    def alive(self):
        return self.health > 0
    def print_status(self):
        print('{} currently has {} hp.'.format(self.name, self.health))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 25
        self.power = 7
        self.armor = 1
        self.coins = 20
    def attack(self, enemy):
        probability = random.randint(1, 100)
        if probability <= 20:
            enemy.health -= self.power * 2
        print("{} attacks {}".format(self.name, enemy.name))
        time.sleep(0.5)
    def receive_damage(self, points):
        points -= self.armor
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))
    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 15
        self.power = 3
    def receive_damage(self, points):
        self.health -= points
        probability = random.randint(1, 100)
        print("{} received {} damage.".format(self.name, points))
        if probability <= 20:
            self.health += 2
        elif self.health <= 0:
            print("{} is dead.".format(self.name))

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
    def receive_damage(self, points):
        probability = random.randint(1, 100)
        if probability <= 10:
            self.health -= points
            print("{} received {} damage.".format(self.name, points))
        elif self.health <= 0:
            print("{} is dead.".format(self.name))

class Sorcerer(Character):
    def __init__(self):
        self.name = 'sorcerer'
        self.health = 15
        self.power = 10
    def receive_damage(self, points):
        probability = random.randint(1, 100)
        if probability <= 50:
            self.health -= points
            print("{} received {} damage.".format(self.name, points))
        elif self.health <= 0:
            print("{} is dead.".format(self.name))

class Knight(Character):
    def __init__(self):
        self.name = 'knight'
        self.health = 20
        self.power = 8
    def receive_damage(self, points):
        probability = random.ranint(1, 100)
        if probability <= 90:
            self.health -= points
            print("{} received {} damage".format(self.name, points))
        elif self.health <= 0:
            print("{} is dead.".format(self.name))

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 10
        self.power = 4
    def alive(self):
        return self.health > 0

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 3
    def alive(self):
        return self.health <= 10

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(0.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
                hero.receive_damage
                enemy.receive_damage
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            return True
        else:
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class SuperTonic(object):
    cost = 10
    name = 'supertonic'
    def apply(self, character):
        character.health += 10
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print("{}'s armor increased to {}.".format(hero.name, hero.armor))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Armor]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            inpt = int(input("> "))
            if inpt == 10:
                break
            else:
                ItemToBuy = Store.items[inpt - 1]
                item = ItemToBuy()
                hero.buy(item)

# This replaces main()
if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Zombie()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("You lose!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("You win!")
