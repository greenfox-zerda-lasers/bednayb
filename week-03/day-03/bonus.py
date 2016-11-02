a = "*"

maxstar = 6;

i = 0;
j = 0;

for j  in range(2):

    if j == 1:
        while i>0:
            print (a*(i-1))
            i -= 1;
            if i == 0:
                exit()

    for i in range(maxstar):
        print (a*i)
        if i == 5:
            j += 1;
