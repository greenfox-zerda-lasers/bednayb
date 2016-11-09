import random


from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(size):

    x = 0
    y = 0


    for i in range(5):
        lime_box = canvas.create_rectangle( size * (2**i - 1), size*(2**i-1), size*(2**(i+1)-1), size*(2**(i+1)-1), fill="purple")




square_maker(10)
root.mainloop()
