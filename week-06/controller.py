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
        self.skeltons = character.Skeleton()
        self.view.display_map(self.map.board)
        self.boss_position()
        self.skeletons_position()
        self.battle = Battle(self.hero, self.boss)



        self.input_event()
        self.view.display_hero_down(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        self.view.root.mainloop()

        ### BOSS POSITION ###                                ### IN THE FUTURE MOVE TO THE CHARACTERS ###
    def boss_position(self):
        x_pos = random.randint(0,9)
        y_pos = random.randint(0,8)

        while self.map.board[y_pos][x_pos] != 1:
            print("wall")
            print("y",y_pos)
            print("x",x_pos)
            x_pos += random.randint(-1,1)
            y_pos += random.randint(-1,1)
            #  x_pos = random.randint(0,9)
            #  y_pos = random.randint(0,10)

        self.view.display_boss(x_pos,y_pos)
        self.boss.x_pos = x_pos
        self.boss.y_pos = y_pos

    def boss_move(self):

        x_pos = self.boss.x_pos
        y_pos = self.boss.y_pos


        # while self.map.board[self.boss.y_pos][self.boss.x_pos] == 1 and (x_pos != self.boss.x_pos):
        self.korte = random.randint(1,4)
        if self.korte == 1:
            self.boss.x_pos += 1
        elif self.korte == 2:
            self.boss.y_pos += 1
        elif self.korte == 3:
            self.boss.x_pos -= 1
        elif self.korte == 4:
            self.boss.y_pos -= 1

        if self.boss.x_pos < 0 or self.boss.y_pos < 0 or self.boss.x_pos > 9 or self.boss.y_pos > 10:
            self.boss.x_pos = x_pos
            self.boss.y_pos = y_pos
            self.boss_move()
            return

        if self.map.board[self.boss.y_pos][self.boss.x_pos] != 1:
            self.boss.x_pos = x_pos
            self.boss.y_pos = y_pos
            self.boss_move()
            return



        self.view.display_floor(72 + x_pos * self.view.size, 72 + y_pos * self.view.size)
        self.view.display_boss(self.boss.x_pos,self.boss.y_pos)
        print("BX",self.boss.x_pos)
        print("BY",self.boss.y_pos)
        ### SKELETON NUMBERS AND POSITION ###



    def skeletons_position(self):
        skeleton_numbers = random.randint(2,5)

        for i in range(skeleton_numbers):
            x_pos = random.randint(0,9)
            y_pos = random.randint(0,8)

            while self.map.board[y_pos][x_pos] != 1:
                print("wall")
                print("y",y_pos)
                print("x",x_pos)
                x_pos += random.randint(-1,1)
                y_pos += random.randint(-1,1)
            self.view.display_skeleton(x_pos,y_pos)









        ### HERO MOVING ###


    def input_event(self):
        self.view.root.bind('<s>', self.move_down)
        self.view.root.bind('<w>', self.move_up)
        self.view.root.bind('<a>', self.move_left)
        self.view.root.bind('<d>', self.move_right)


        ### CODE ###
        self.view.root.bind('<p>', self.code_of_game)



    def code_of_game(self, event):

        if event.char == "p":
            code = input("write a code")

            if code == "kiki":
                print("You are immortal")
        ### END OF THE CODE ###

    def move_down(self, event):

        if event.char == "s":




            if self.map.board[self.hero.y_pos + 1][self.hero.x_pos] != 1 or self.hero.y_pos == 10:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.y_pos += 1
                 self.draw_game_map("down")
                 self.battle.fight()
                 self.boss_move()
                 self.battle.fight()
                 self.finish_him()

    def move_up(self,event):

        if event.char == "w":



            if self.map.board[self.hero.y_pos - 1][self.hero.x_pos] != 1 or self.hero.y_pos == 0:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.y_pos -= 1
                 self.draw_game_map("up")
                 self.battle.fight()
                 self.boss_move()
                 self.battle.fight()
                 self.finish_him()

    def move_left(self,event):

        if event.char == "a":



            if self.map.board[self.hero.y_pos ][self.hero.x_pos - 1] != 1 or  self.hero.x_pos == 0:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.x_pos -= 1
                 self.draw_game_map("left")
                 self.battle.fight()
                 self.boss_move()
                 self.battle.fight()
                 self.finish_him()

    def move_right(self,event):

        if event.char == "d":



            if self.map.board[self.hero.y_pos][self.hero.x_pos + 1] != 1 or self.hero.x_pos == 11:

                print("wall")

            else:
                 self.view.display_floor(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
                 self.hero.x_pos += 1
                 self.draw_game_map("right")
                 self.battle.fight()
                 self.boss_move()
                 self.battle.fight()
                 self.finish_him()


    def draw_game_map(self,direction):
        if direction == "right":
            self.view.display_hero_right(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "down":
            self.view.display_hero_down(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "left":
            self.view.display_hero_left(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)
        if direction == "up":
            self.view.display_hero_up(72 + self.hero.x_pos * self.view.size, 72 + self.hero.y_pos * self.view.size)

            ### END OF HERO MOVING ###



        ### FINISH HIM ###

    def finish_him(self):
        if self.boss.hp <= 0:
            self.view.display_finishhim()




x = Control()
# x.start_the_game()
# x.fight()
