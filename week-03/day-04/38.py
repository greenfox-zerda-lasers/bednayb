numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def find_the_min(listname):
    min_number = listname[0]
    for i in range(len(listname)):
        if min_number > listname[i]:
            min_number = listname[i]
    print(min_number)

find_the_min(numbers)
