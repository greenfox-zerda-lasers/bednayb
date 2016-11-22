from tkinter import *
from PIL import Image, ImageTk



class View():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(width=720, height = 792, bg="black")
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")

        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")

        self.skeleton = PhotoImage(file = "skeleton.png")
        self.boss = PhotoImage(file = "boss.png")


    def display_map(self,Game_Map):

        for i in range(9):
            for j in range(10):
                if Game_Map[j][i] == 1:
                    self.canvas.create_image(36+i*72, 36+j*72, image = self.floor)
                else:
                    self.canvas.create_image(36+i*72, 36+j*72, image = self.wall)

    # def hero_view(self, hero_x_pos,hero_y_pos):
    #
    #     self.canvas.create_image(36+i*72, 36+j*72, image = self.hero_down)
