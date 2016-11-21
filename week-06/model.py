### MODEL ###

from PIL import Image, ImageTk
import random

### MAP OF THE GAME ###

class Map():

    Wall= 1
    Floor = 0

    map_game = [
    [Floor,Floor,Floor,Wall,Floor,Wall,Floor,Floor,Floor,Floor],
    [Floor,Floor,Floor,Wall,Floor,Wall,Floor,Wall,Wall,Floor],
    [Floor,Wall,Wall,Wall,Floor,Wall,Floor,Wall,Wall,Floor],
    [Floor,Floor,Floor,Floor,Floor,Wall,Floor,Floor,Floor,Floor],
    [Wall,Wall,Wall,Wall,Floor,Wall,Wall,Wall,Wall,Floor],
    [Floor,Wall,Floor,Wall,Floor,Floor,Floor,Floor,Wall,Floor],
    [Floor,Wall,Floor,Wall,Floor,Wall,Wall,Floor,Wall,Floor],
    [Floor,Floor,Floor,Floor,Floor,Wall,Wall,Floor,Wall,Floor],
    [Floor,Wall,Floor,Wall,Floor,Wall,Wall,Floor,Wall,Floor],
    [Floor,Floor,Floor,Wall,Floor,Wall,Wall,Floor,Wall,Floor],
    [Floor,Wall,Floor,Wall,Floor,Wall,Floor,Floor,Floor,Floor],
    ]



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
        self.strike = 5 + random.randint(1,6)
        self.current_hp = self.max_hp

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass


class Enemy(Characters):
    pass


class Skeleton(Enemy):
    def __init__(self):
        self.level = 1
        self.max_hp = 2 * self.level * random.randint(1,6)
        self.defence = self.level / 2 * random.randint(1,6)
        self.strike = self.level * random.randint(1,6)
        self.current_hp = self.max_hp

class Boss(Enemy):
    def __init__(self):
        self.level = 1
        self.max_hp = 2 * self.level * random.randint(1,6) + random.randint(1,6)
        self.current_hp = self.max_hp
        self.defence = self.level / 2 * random.randint(1,6) + random.randint(1,6) /2
        self.strike = random.randint(1,6) + self.level

class Skeleton_with_key(Skeleton):
    pass

### BATTLE ###

x = Hero()

print(x.level)
