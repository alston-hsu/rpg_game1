class Character(object):
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print(self.health)

class Hero(Character):
    def __init__(self):
        self.health = 25
        self.power = 7
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True

class Goblin(Character):
    def __init__(self):
        self.health = 10
        self.power = 4
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True

def main():
    goblin = Goblin()
    hero = Hero()

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

if __name__ == "__main__":
  main()
