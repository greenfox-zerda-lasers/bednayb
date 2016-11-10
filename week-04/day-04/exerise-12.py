# 12. write a recursive function that can add numbers in


list1 = [1, 2, [3, 4], 1, [1, [2, 4]]]



def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

x = listsum(list1)

print(x)
