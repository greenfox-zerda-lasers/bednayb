

from tkinter import *

root = Tk()

canvas = Canvas(root, bg="black", width='300', height='300')
canvas.pack()



teal_line =  canvas.create_line(0, 150, 300,150, fill='red')
teal_line2 = canvas.create_line(150, 0, 150, 300, fill='green')

root.mainloop()
