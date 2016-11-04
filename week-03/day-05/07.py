# create a function that takes a list and returns a new list with all the elements doubled

class Doubled:

    def reversed(self,elements):

        reverse = []
        for i in range( len(elements)):
            reverse.append(elements[i]*2)
        return reverse



numbers = [4,5,6,7]

magic = Doubled()


print(magic.reversed(numbers))
