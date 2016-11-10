# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n


def addition(number):

    if number == 1:
        return number
    else:

        return number + addition(number-1)
    return result


print( addition(998))
