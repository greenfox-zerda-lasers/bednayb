# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='1200', height='1200')
canvas.pack()

def strange ():
    for i in range(15):
        teal_line = canvas.create_line(0, 300-i*20, 300-i*20, 300, fill='green')
        teal_line = canvas.create_line(20*i, 0, 300, i*20, fill='purple')


strange()
root.mainloop()
