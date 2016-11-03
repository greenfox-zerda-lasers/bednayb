

list10 =[4,5,6,11,22,22,45]
list11 =[4,5,7,11,23]
list12=[1,2,3]
list12=[4,1,7]





def unio_once(list1, list2):

    list3 = list1 + list2
    list4 =[]
    for i in range(len(list3)):
        if list3[i] not in list4:
            list4.append(list3[i])
    return list4



result = unio_once(list10,list11)

print(result)
