# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle:

    def circumference(radius):
        a = radius * 2 *3.14
        return a

    def get_area(radius):
        a = radius ** 2 *3.14
        return a


print(Circle.get_area(30))
print(Circle.circumference(30))
