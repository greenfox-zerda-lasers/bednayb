from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

teal_line = canvas.create_line(10, 10, 10, 100, fill='green')
teal_line2 = canvas.create_line(10, 100, 100, 100, fill='red')
lime_box = canvas.create_line(100, 100, 100, 10, fill='blue')
olive_oval = canvas.create_line(100, 10, 10,10, fill='yellow')

root.mainloop()


# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
