numbers = [1,2,3,4,5,6,7,8,9,11,13]

i = 0
oddnumbers = 0
evennumbers = 0

while  i < len(numbers):
    if numbers[i] % 2 == 1:
        oddnumbers += 1
        i = i + 1
    elif numbers[i] % 2 == 0:
        evennumbers += 1
        i = i + 1


print(oddnumbers)
print(evennumbers)
