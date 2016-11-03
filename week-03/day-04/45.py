filename = 'alma.txt'
# Write the numbers from 1 to 10 to the file stored in filename



def Palindome(listname):
    copylist = []
    i = 1
    while i < (len(listname) + 1 ):
        copylist.append(listname[-i])
        i = i + 1
    print(copylist)

Palindome("Fox")
