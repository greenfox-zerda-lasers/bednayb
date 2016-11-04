# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

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
