from tkinter import *
import time
import random


root = Tk()

canvas = Canvas(root, bg="black", width='600', height='600')
canvas.pack()

a=10

def magic(x,y,number,size,number_begin):
    # if number_begin == number:
    #     topleft = ( 0, a+0)
    #     topright = (size,a+0)
    #     bottom = ( size*(3**0.5)/3.46, a+size*(3**0.5)/2)
    #     canvas.create_polygon(topleft, topright, bottom, fill='white', outline='purple')

    if number == 1:
        return 1
    else:

        teal_line = canvas.create_line(x + size*1/2,a+ y + 0,  x + size *1/4,a+ y + size*(3**0.5)/4,fill='blue')
        teal_line = canvas.create_line(x + size*1/2, a+y + 0,  x + size *3/4, a+y + size*(3**0.5)/4,fill='red')
        teal_line = canvas.create_line( x + size *1/4 ,a+ y + size*(3**0.5)/4,  x + size *3/4, a+y + size*(3**0.5)/4,fill='green')

        number -= 1
    #
    #     magic(x,y,number,size/2,number_begin)
    #     magic(x+size/2,y,number,size/2,number_begin)
    #     magic(x+size/4,y+size*(3**0.5)/4,number,size/2,number_begin)
    #
    #
    #
    time.sleep(0.01)
    canvas.update()


canvas.create_text(300,550,fill="green",font="Times 30 italic bold",text="GREENFOX")



magic(0,0,7,600,7)

def input_event(self):
        self.view.root.bind('<s>', self.root.mainloop())
