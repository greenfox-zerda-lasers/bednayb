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
    
        teal_line = canvas.create_line(100, 30, 150, 115 )
        teal_line = canvas.create_line(150, 115, 50, 115 )
        teal_line = canvas.create_line(50, 115, 100, 30)




square_maker(10)
root.mainloop()
