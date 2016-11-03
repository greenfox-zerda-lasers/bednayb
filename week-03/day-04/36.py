numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def reverse(listname):
    copylist = []
    i = 1
    while i < (len(listname) + 1 ):
        copylist.append(listname[-i])
        i = i + 1
    print(copylist)

reverse(numbers)
