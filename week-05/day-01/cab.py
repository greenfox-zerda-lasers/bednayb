import random

number = random.randrange(1000)
number= str (number)
number = list(number)
number = [int(i) for i in number]

print(number)


def cab(a,b,c):
    if a == number[0]:
     print("bull")
    if b == number[1]:
     print("bull")
    if c == number[2]:
     print("bull")

print(number[0])

cab(1,2,3)
