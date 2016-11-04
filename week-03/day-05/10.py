# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def star_number(number):
        for i in range(1,number+1,2):
            print(" " * ((number-i)//2) , "*" * i, " " * ((number-i)//2))

star_number(11)
