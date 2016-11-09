
# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.


from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(size):
    lime_box = canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, )


square_maker(150)
square_maker(100)
square_maker(50)
root.mainloop()
