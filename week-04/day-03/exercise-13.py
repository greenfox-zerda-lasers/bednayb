# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_drawing(x,y):

    teal_line = canvas.create_line(x, y, 150, 150, fill='green')



for i in range(15):
    line_drawing(20*i,0)
    line_drawing(0,20*i)
    line_drawing(20*i,300)
    line_drawing(300, 20*i)



root.mainloop()
