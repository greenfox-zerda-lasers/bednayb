# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has



def star_number(number):

        for i in range(1,number+1,2):
                print(" " * ((number-i)//2) , "*" * i, " " * ((number-i)//2))

        for i in range(number-2,0,-2):
                print(" " * ((number-i)//2) , "*" * i, " " * ((number-i)//2))

star_number(31)
