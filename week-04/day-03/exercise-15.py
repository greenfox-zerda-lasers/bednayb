# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]


from tkinter import *

root = Tk()

list1 = [[10, 10], [290,  10], [290, 290], [10, 290]]
list2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker():
    for i in range(4):
        lime_box = canvas.create_rectangle(list1[i][i], list1[i][i+1], x+size, y+size, fill=color)
        lime_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)
        lime_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)
        lime_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)



print(list1[0][0])
