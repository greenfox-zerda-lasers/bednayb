from tkinter import *
from math import *

base = Tk()

size = 600

canvas = Canvas(base, width=size, height=size, bg="white")
canvas.pack()

def draw_hexagon(side, x, y):
    top_left = canvas.create_line(x, y, x+side, y)
    top_right = canvas.create_line(x+side, y, x+side+side/2, y - (3**0.5)/2*side)
    middle_left = canvas.create_line(x, y-(3**0.5)/2*side*2, x-side/2, y-3**0.5/2*side)
    middle_right = canvas.create_line(x-side/2, y-(3**0.5)/2*side, x, y)
    bottom_left = canvas.create_line(x+side+side/2, y-(3**0.5)/2*side, x+side, y-(3**0.5)/2*side*2)
    bottom_right = canvas.create_line(x+side, y-(3**0.5)/2*side*2, x, y-3**0.5/2*side*2)

def hexa(x, y, size, n):
    if n == 0:
        return 1
    else:
        draw_hexagon(size/3, x, y)

        hexa(x, y, size/3, n-1)
        hexa(x, y-size/3*(3**0.5/2)*4/3, size/3, n-1)
        hexa(x+size/3*(2/3), y, size/3, n-1)
        hexa(x+size/3*(2/3), y-size/3*(3**0.5/2)*4/3, size/3, n-1)
        hexa(x-size/3*(1/3), y-size/3*(2/3)*(3**0.5/2), size/3, n-1)
        hexa(x+size/3, y-size/3*(2/3)*(3**0.5/2), size/3, n-1)


hexa(size/4, size/1.2, 700, 5)

base.mainloop()
