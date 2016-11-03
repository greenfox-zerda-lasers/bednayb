# create a function that returns it's input factorial


def factorial(number_factorial):
    summa = 1
    i = 1
    while i < number_factorial+1:
        summa = summa * i
        i = i + 1
        print(summa)

factorial(5)
