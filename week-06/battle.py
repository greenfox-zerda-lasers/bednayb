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

            print("h s",self.hero.strike * random.randint(1,6))
            print("h s",self.hero.strike * random.randint(1,6))
            print("h s",self.hero.strike * random.randint(1,6))


            print("b s",self.boss.strike)
            print("h d",self.hero.defence)
            print("b d",self.boss.defence)
            print("h m hp",self.hero.max_hp)
