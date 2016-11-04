# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def star_number(number):
    for i in range(1,number+1):
        print("*" * i)

star_number(6)
