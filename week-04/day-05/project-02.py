from tkinter import *
import time
import random


root = Tk()

canvas = Canvas(root, bg="lightgray", width='600', height='600')
canvas.pack()


def text():
    canvas.create_text(200,100,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")

text()

root.mainloop()
