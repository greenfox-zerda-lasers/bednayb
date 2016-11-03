names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def find_the_shortest_string(listname):
    shortest_name = listname[0]
    for i in range(len(listname)):
        if len(shortest_name) > len(listname[i]):
            shortest_name = listname[i]
    return shortest_name



result = find_the_shortest_string(names)

print(result)
