from tkinter import *

root = Tk()

canvas = Canvas(root, bg="yellow", width='600', height='600')
canvas.pack()


def magic(x,y,number,size):
    if number == 1:
        return 1
    else:
        teal_line = canvas.create_line(x + size*1/3, y + 0,  x + size *1/3, y + size)
        teal_line = canvas.create_line(x + size*2/3, y + 0,  x + size *2/3, y + size)
        teal_line = canvas.create_line(x + 0, y + size*1/3, x + size, y + size *1/3)
        teal_line = canvas.create_line(x + 0, y + size*2/3, x + size, y + size *2/3)

        magic( 0+x,  y + size*1/3, number-1, size*1/3 )
        magic( x+size*1/3,  0+y, number-1, size*1/3 )
        magic( x+size*1/3,  y+size*2/3, number-1, size*1/3 )
        magic( x+size*2/3,  y+size*1/3, number-1, size*1/3 )


        

magic(0,0,6,600)
root.mainloop()
