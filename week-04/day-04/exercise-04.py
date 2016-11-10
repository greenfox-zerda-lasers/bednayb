# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power(x, y):
    if y == 0:
        return 1
    else:
        return x*power(x, y-1)


x = power(3,3)

print(x)
