# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.


from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(x,y,size,color):
    lime_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)


square_maker(10,10,50,"red")
square_maker(110,110,50,"blue")
square_maker(110,110,50,"yellow")





root.mainloop()


# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
