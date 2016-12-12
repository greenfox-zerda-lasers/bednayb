from tkinter import *

root = Tk()

canvas = Canvas(root, bg="black", width='600', height='600')
canvas.pack()


def magic(x,y,number,size):
    if number == 1:
        return 1
    else:
        # teal_line = canvas.create_line(x + size*1/3, y + 0,  x + size *1/3, y + size)
        # teal_line = canvas.create_line(x + size*2/3, y + 0,  x + size *2/3, y + size)
        # teal_line = canvas.create_line(x + 0, y + size*1/3, x + size, y + size *1/3)
        # teal_line = canvas.create_line(x + 0, y + size*2/3, x + size, y + size *2/3)

        teal_line = canvas.create_line(0, , 0, 1,fill='blue')
        teal_line = canvas.create_line(x + size*1/2,   0,  x + size *3/4, size*(3**0.5)/4,fill='red')
        teal_line = canvas.create_line( x + size *1/4 , size*(3**0.5)/4,  x + size *3/4, size*(3**0.5)/4,fill='green')



magic(0,0,6,600)
root.mainloop()
