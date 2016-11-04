# Create a class called "Car"
# It should have a "type" property that stores the car's type in a string eg: "Mazda"
# It should have a "km" property that stores how many kilometers it have run
# The km and the type property should be a parmeter in the constructor
# It should have a method called "run" that takes a number and increments the "km" property by it

class Car:
    km = 0
    type = " "
    
    def type(self):
        return carType


    def ride(self):
        return km





my_mazda = Car("mazda", 12000)
my_mazda.ride(100)
print(my_mazda.type) # "mazda"
print(my_mazda.km) # 12100


class Pirate:
    rum = 0

    def drink_rum(self):
        self.rum += 1


    def hows_goin_mate(self):
        if self.rum == 5:
            print("Arrrr!")
        else:
            ("Nothin")


act = Pirate()


act.drink_rum()
act.drink_rum()
act.drink_rum()
act.drink_rum()
act.drink_rum()
act.hows_goin_mate()
