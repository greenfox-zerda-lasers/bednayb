# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import random
import model_elevator
import view_elevator
import os




class Controller():

    def __init__(self):
        self.Elevator = model_elevator.Elevator(10,0,1)
        self.View = view_elevator.View(10,7,2)


    def add_people(self):
        self.Elevator.people += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        self.View.Picture(self.Elevator.all_levels,self.Elevator.current_level,self.Elevator.people)

    def remove_people(self):
        self.Elevator.people -= 1
        os.system('cls' if os.name == 'nt' else 'clear')
        self.View.Picture(self.Elevator.all_levels,self.Elevator.current_level,self.Elevator.people)

    def move_up(self):
        self.Elevator.current_level += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        self.View.Picture(self.Elevator.all_levels,self.Elevator.current_level,self.Elevator.people)

    def move_down(self):
        self.Elevator.current_level -= 1
        os.system('cls' if os.name == 'nt' else 'clear')
        self.View.Picture(self.Elevator.all_levels,self.Elevator.current_level,self.Elevator.people)

x = Controller()






while True:



    print(" ")
    print("up ------------- u")
    print("down ----------- d")
    print("new person ----- n")
    print(" a person left - l")

    answer = input("up or down, more or less\n")
    if answer == "u":
        x.move_up()
    if answer == "d":
        x.move_down()
    if answer == "n":
        x.add_people()
    if answer == "l":
        x.remove_people()





# def rampage_mode(self):
#
#     self.Elevator.current_level = random.randint(0,self.Elevator.all_levels)
#     if self.Elevator.people > 1:
#         death = random.randint(1,self.Elevator.people-1)
#         self.Elevator.people -= death
#         print("After the rampage mode",death,"people died but don't worry",self.Elevator.people,"left. Anyway the stage is", self.Elevator.current_level)
#
#     self.View.Picture(self.Elevator.all_levels,self.Elevator.current_level,self.Elevator.people)



# self.current_level = random.randint(0,self.all_levels)
# if self.people > 1:
#     death = random.randint(1,self.people-1)
#     self.people -= death
#     print("After the rampage mode",death,"people died but don't worry",self.people,"left. Anyway the stage is", self.current_level)
