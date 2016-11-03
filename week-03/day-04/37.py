numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def find_even_numbers(listname):
    even_numbers = []
    for i in range(len(listname)):
        if listname[i] % 2 == 0:
            even_numbers.append(listname[i])
    return even_numbers

the_even_numbes = find_even_numbers(numbers)

print(the_even_numbes)
