# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

import random

blue = random.randint(0, 255)
red = random.randint(0, 255)
green = random.randint(0, 255)



from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(size,color):
    for i in range(1,20):
        if i % 2 == 0:
            lime_box = canvas.create_rectangle(0+size, 0+size, 300-size, 300-size, fill = "red")
        else:
            lime_box = canvas.create_rectangle(0+size, 0+size, 300-size, 300-size, fill = color)
        size += 8


square_maker(5,"blue")
root.mainloop()
