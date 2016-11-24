from tkinter import *
from PIL import Image, ImageTk




class View():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1200, height = 900, bg="black")
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.size = 72

        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")

        self.skeleton = PhotoImage(file = "skeleton.png")
        self.boss = PhotoImage(file = "boss.png")

        self.finish_him = PhotoImage(file = "finish.png")

    ### DISPLAY MAP ###
    def display_map(self,Game_Map):

        for i in range(10):
            for j in range(11):
                if Game_Map[j][i] == 1:
                    self.canvas.create_image(self.size+i*self.size, self.size+j*self.size, image = self.floor)
                else:
                    self.canvas.create_image(self.size+i*self.size, self.size+j*self.size, image = self.wall)

    ### DISPLAY HERO ###

    def display_hero_down(self, hero_x_pos,hero_y_pos):
        self.canvas.create_image(hero_x_pos, hero_y_pos, image = self.hero_down)

    def display_hero_up(self, hero_x_pos,hero_y_pos):
        self.canvas.create_image(hero_x_pos, hero_y_pos, image = self.hero_up)

    def display_hero_right(self, hero_x_pos,hero_y_pos):
        self.canvas.create_image(hero_x_pos, hero_y_pos, image = self.hero_right)

    def display_hero_left(self, hero_x_pos,hero_y_pos):
        self.canvas.create_image(hero_x_pos, hero_y_pos, image = self.hero_left)

    ### DISPLAY ENEMY ###

    def display_boss(self, boss_x_pos,boss_y_pos):

        self.canvas.create_image(72 + (boss_x_pos)  * self.size, 72 + (boss_y_pos) * self.size, image = self.boss)
        print(boss_x_pos)
        print(boss_y_pos)

    def display_skeleton(self, skeleton_x_pos,skeleton_y_pos):

        self.canvas.create_image(72 + (skeleton_x_pos)  * self.size, 72 + (skeleton_y_pos) * self.size, image = self.skeleton)


   ### DISPLAY FLOOR ###


    def display_floor(self, hero_x_pos,hero_y_pos):
        self.canvas.create_image(hero_x_pos, hero_y_pos, image = self.floor)

    ### DISPLAY BATTLE ###

    def battle_view(self):
        self.canvas.create_image(1000, 800, image = self.floor)

    ## DISPLAY FINISH HIM ###

    def display_finishhim(self):
        self.canvas.create_image(900, 100, image = self.finish_him)
