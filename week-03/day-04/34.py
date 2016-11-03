numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def sum(list_sum):
    summa = 0
    for i in range(len(list_sum)):
        summa += list_sum[i]
    print(summa)

sum(numbers)
