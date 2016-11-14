# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if (a >= b and a > c) or (a > b and a >= c):
        return a

    elif (b >= a and b > c) or (b > c and a >= a):
        return b
    elif (c >= a and c > b) or (c > b and c >= a):
        return c

# Returns the median value of a list given as param
def median(pool):
    pool = sorted(pool)
    if len(pool) % 2 == 0:
        j = int(len(pool)/2)
        return (pool[j-1]+ pool[j])/2

    else:
        i = int(len(pool)/2 )
        return pool[i]




# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    teve2 = []
    for char in teve:
        if is_vovel(char):
            teve2.append( (char+'v'+char))
        else:
            teve2.append(char)
    return "".join(teve2)

translate("almabake")
