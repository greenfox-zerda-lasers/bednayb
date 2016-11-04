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
    for j  in range(2):
        if j == 0:
            step = 2
        else:
            step = 1
        for i in range(1,number+1,step):
            if j == 1:
                print(" " * (i) , "*" * (number-(i*2)), " " * (i))
                if i == number+1:
                    j += 1;

            if j == 0:
                print(" " * ((number-i)//2) , "*" * i, " " * ((number-i)//2))

star_number(31)
