# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods


class Stack:
    elements = ["alma","5"]

    def size(self):
        return len(self.elements)

    def pop(self):
        self.elements = self.elements[:-1]
        return len(self.elements)


    def push(self, push_elements):
        self.elements = self.elements + [push_elements]
        return self.elements


magic = Stack()

magic.pop()
magic.push('alma')
magic.push('alma')
magic.push('alma')

print(magic.size())
