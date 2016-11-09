# create a 300x300 canvas.
# fill it with four different size and color rectangles.


from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(x,y,size,color):
    lime_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)


square_maker(10,10,50,"red")
square_maker(110,110,50,"blue")
square_maker(210,210,50,"yellow")
square_maker(210,110,50,"green")
root.mainloop()
