# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

import random



class Elevator():

    def __init__(self,all_levels,current_level,people):
        self.all_levels = all_levels
        self.current_level =current_level
        self.people = people


    def position(self):
        print("Stage", self.current_level,"People", self.people)


    def people_count(self):
        print(self.people)

    def add_people(self):
        self.people += 1

    def remove_people(self):
        if self.people > 0:
            self.people -= 1

    def move_up(self):
        if self.current_level < self.all_levels:
            self.current_level += 1

    def move_down(self):
        if self.current_level > 0:
            self.current_level -= 1

    def rampage_mode(self):
        self.current_level = random.randint(0,self.all_levels)
        if self.people > 1:
            death = random.randint(1,self.people-1)
            self.people -= death
            print("After the rampage mode",death,"people died but don't worry",self.people,"left. Anyway the stage is", self.current_level)


# x = Elevator(10,0,5)

# x.position()
# x.add_people()
# x.add_people()
# x.position()
# x.remove_people()
# x.move_up()
# x.remove_people()
# x.remove_people()
# x.position()
# x.rampage_mode()
# x.move_down()
# x.position()
