from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def strange ():
    for i in range(30):
        teal_line = canvas.create_line(0, 300-i*20, 300-i*20, 300, fill='green')
        teal_line = canvas.create_line(20*i, 0, 300, i*20, fill='purple')


strange()
root.mainloop()
