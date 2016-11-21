alma = [2,3,4,5]


def median(pool):
    if len(pool) % 2 == 0:
        j = int(len(pool)/2)
        print((pool[j-1]+ pool[j])/2)

    else:
        i = int(len(pool)/2 )
        print(pool[i])

median(alma)
