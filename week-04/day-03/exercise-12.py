# create a 300x300 canvas.
# fill it with a checkerboard pattern.


from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' )
canvas.pack()

def chess_board(size):

    for i in range(0,300,size*2):
        for j in range(0,300,size*2):
            lime_box = canvas.create_rectangle(i, j, i+size, j+size, fill="black")

    for i in range(size,300,size*2):
        for j in range(size,300,size*2):
            lime_box = canvas.create_rectangle(i, j, i+size, j+size, fill="black")






chess_board(10)
root.mainloop()
