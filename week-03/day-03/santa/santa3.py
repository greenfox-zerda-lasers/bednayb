

fname = "C:\greenfox\git\\bednayb\greenfox\\bednayb\week-03\day-03\santa\present.txt"

biglist = []

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        biglist.append((line.rstrip().split("x")))

print(biglist)

for i in range(len(biglist)):
    for j in range()
