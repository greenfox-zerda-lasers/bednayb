# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)



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
