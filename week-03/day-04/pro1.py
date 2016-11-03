
list3 = [4,5,3,4,5,1,1,1,1,6]
list2 = [4,5,7]

def linear_search(list, number):
    
    for i in range(len(list)):
        if number == list[i]:
            return i
    return -1



result = linear_search(list3, 6)

print(result)
