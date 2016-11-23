from view import View
import map_of_game
import character
import tkinter
from battle import Battle


import random


class Control:
    def __init__(self):
        self.map = map_of_game.Game_Map()
        self.view = View()
        self.hero = character.Hero()
        self.boss = character.Boss()
        self.view.display_map(self.map.board)
        self.boss_position()
        self.battle = Battle(self.hero, self.boss)


        self.input_event()
        self.view.display_hero_down(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        self.view.root.mainloop()


    def boss_position(self):
        self.view.display_boss(self.boss.x_pos,self.boss.y_pos)







    def draw_game_map(self,direction):
        if direction == "right":
            self.view.display_hero_right(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "down":
            self.view.display_hero_down(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "left":
            self.view.display_hero_left(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "up":
            self.view.display_hero_up(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)


    ### HERO MOVING ###


    def input_event(self):
        self.view.root.bind('<s>', self.move_down)
        self.view.root.bind('<w>', self.move_up)
        self.view.root.bind('<a>', self.move_left)
        self.view.root.bind('<d>', self.move_right)

    def move_down(self, event):

        if event.char == "s":




            if self.map.board[self.hero.y_pos + 1][self.hero.x_pos] != 1 or self.hero.y_pos == 10:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.y_pos += 1
                 self.draw_game_map("down")
                 self.battle.fight()


    def move_up(self,event):

        if event.char == "w":



            if self.map.board[self.hero.y_pos - 1][self.hero.x_pos] != 1 or self.hero.y_pos == 0:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.y_pos -= 1
                 self.draw_game_map("up")
                 self.battle.fight()


    def move_left(self,event):

        if event.char == "a":



            if self.map.board[self.hero.y_pos ][self.hero.x_pos - 1] != 1 or  self.hero.x_pos == 0:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.x_pos -= 1
                 self.draw_game_map("left")
                 self.battle.fight()

    def move_right(self,event):

        if event.char == "d":



            if self.map.board[self.hero.y_pos][self.hero.x_pos + 1] != 1 or self.hero.x_pos == 11:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.x_pos += 1
                 self.draw_game_map("right")
                 self.battle.fight()





### Battle  ###

    # def fight(self):
    #     print(self.hero.strike)




x = Control()
# x.start_the_game()
# x.fight()
