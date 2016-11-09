# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(size):
    for i in range(1,20):
        lime_box = canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2)
        size += 295/20


square_maker(10)
root.mainloop()
