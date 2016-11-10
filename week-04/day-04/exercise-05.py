# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def bunny_ear(bunny):
    if bunny == 1:
        return 2
    else:
        return 2 + bunny_ear(bunny-1)


x = bunny_ear(8)

print(x)
