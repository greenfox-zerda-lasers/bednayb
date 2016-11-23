### MODEL ###

import random
import map_of_game
from view import View


### CHARACTERS ###

class Characters:

        level = 4
        max_hp = 10
        current_hp = 10
        defence = 10
        strike = 10

class Hero(Characters):
    def __init__(self):

        self.level = 1
        self.max_hp = 20 + 3 * random.randint(1,6)

        self.defence = 2 * random.randint(1,6)
        self.strike = 5
        self.current_hp = self.max_hp
        self.x_pos = 0
        self.y_pos = 0



class Enemy(Characters):
    pass


class Skeleton(Enemy):
    def __init__(self):
        self.level = 1
        self.max_hp = 2 * self.level * random.randint(1,6)
        self.defence = self.level / 2 * random.randint(1,6)
        self.strike = self.level * random.randint(1,6)
        self.current_hp = self.max_hp


        self.map = map_of_game.Game_Map()

class Boss(Enemy):
    def __init__(self):

        self.level = 1
        self.max_hp = 2 * self.level * random.randint(1,6) + random.randint(1,6)
        self.current_hp = self.max_hp
        self.defence = self.level / 2 * random.randint(1,6) + random.randint(1,6) /2
        self.strike = random.randint(1,6) + self.level
        self.map = map_of_game.Game_Map()

        self.x_pos = random.randint(1,10)
        self.y_pos = random.randint(1,11)




class Skeleton_with_key(Skeleton):
    pass

### BATTLE ####

x = Hero()


print(x.level)
