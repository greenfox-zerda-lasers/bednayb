import random



class Battle:
    def Simple_battle(self):
        attack = 6
        defence = 7
        battle_result = random.randint(1, attack + defence)
        if battle_result > defence:
            print(attack)
            print("X win")
        else:
            print("Y win")




class Warriors(Battle):

    attack = 13
    defence = 10
    damage = 10
    health_Point = 20
    experience = 0


class Farmer(Warriors):
    attack = 15
    def stats(self):
        return self.attack



class Calavary(Warriors):
    attack = 25
    def stats(self):
        Soldier_attack = 15


class Artifact:
    sword = 5


magic = Battle()
soldier = Farmer()

soldier.Simple_battle()
