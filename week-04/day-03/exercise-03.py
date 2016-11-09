from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

teal_line = canvas.create_line(0, 0, 300, 300, fill='green')


root.mainloop()


# create a 300x300 canvas.
# draw its diagonals in green.
