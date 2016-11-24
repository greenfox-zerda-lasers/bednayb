import random

import character
from view import View
### Battle ###

class Battle:

    def __init__(self,hero,boss):
        self.hero = hero
        self.boss = boss



    def fight(self):

        ### HERO AND BOSS POSOTION ###



        if self.hero.x_pos == self.boss.x_pos and self.hero.y_pos == self.boss.y_pos:

            while self.hero.current_hp < 0 or self.boss.hp > 0:
                self.hero.strike = self.hero.level * random.randint(1,6)
                self.boss.defence = self.boss.level / 2 * random.randint(1,6) + random.randint(1,6) /2

                self.boss.strike = self.boss.level * random.randint(1,6)
                self.hero.defence = 2 * random.randint(1,6)
                ### ne lehessen tobb mnt volt ###
                if self.hero.strike - self.boss.defence > 0:
                    self.boss.hp -= self.hero.strike - self.boss.defence
                if self.boss.strike - self.hero.defence > 0:
                    self.hero.current_hp -= self.boss.strike - self.hero.defence

                print(" hero strike", self.hero.strike)
                print(" boss defence", self.boss.defence)
                print("boss hp", self.boss.hp)

                print("boss strike", self.boss.strike)
                print("hero defence", self.hero.defence)
                print("hero hp", self.hero.current_hp)

            if self.boss.hp <= 0:
                print("You win")
                
            else:
                print("You died")
