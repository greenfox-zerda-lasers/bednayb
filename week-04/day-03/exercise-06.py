# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

x = 300
y = 300

canvas = Canvas(root, width= x, height= y )
canvas.pack()

def square(x,y,size):
    teal_line = canvas.create_line(x/2 - size/2 , y/2 - size/2,  x/2 + size/2 , y/2 - size/2, fill='green')
    teal_line = canvas.create_line(x/2 - size/2 , y/2 + size/2,  x/2 + size/2 , y/2 + size/2, fill='blue')
    teal_line = canvas.create_line(x/2 + size/2 , y/2 - size/2,  x/2 + size/2 , y/2 + size/2, fill='red')
    teal_line = canvas.create_line(x/2 - size/2 , y/2 + size/2,  x/2 - size/2 , y/2 - size/2, fill='yellow')



square(300,300,10)
root.mainloop()
