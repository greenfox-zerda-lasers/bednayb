
name1 = "Pear"


def Palindome(listname):
    part1 = listname
    part2 = ''
    for i in range(1, len(listname)+1):
        part2 += listname[-i]
    print(part1 + part2)

Palindome(name1)
