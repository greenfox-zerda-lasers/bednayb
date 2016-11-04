# create a function that takes a list and returns a new list that is reversed

class Reversed:

    def reversed(self,elements):

        reverse = []
        for i in range(1, len(elements)+1):
            reverse.append(elements[-i])
        return reverse



colors = ['green','red', 'yellow' ]

magic = Reversed()


print(magic.reversed(colors))
