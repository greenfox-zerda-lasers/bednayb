import random
import math
from decimal import Decimal


class Lotto:

    def __init__(self):
        self.money = 10000
        self.factor = math.factorial


    def lotto_chance(self):

        ### INPUT THE DATA ###
        overall_numbers = input("how many numbers is the pool? ")
        choice_numbers = input("how many numbers need to find out? ")



        ### CONVERT STRING TO NUMBER ###
        overall_numbers = int(overall_numbers)
        choice_numbers = int(choice_numbers)


        if overall_numbers >= choice_numbers and overall_numbers/2 >= choice_numbers:




                ### FIND OUT THE ALL NUMBER ###
            for i in range(0,choice_numbers + 1):

                AB = self.factor(overall_numbers) / self.factor(choice_numbers) / self.factor(overall_numbers - choice_numbers)

                BC = self.factor(choice_numbers) / self.factor(i) / self.factor(choice_numbers - i)

                third = self.factor(overall_numbers - choice_numbers) / self.factor(choice_numbers - i) / self.factor((overall_numbers-choice_numbers) -(choice_numbers - i))

                ### choice_numbers and good tips  with 2 decimal digits###
                print("Your chance to find out exactly", i, "number is 1 to ",round((1/( BC * third / AB)),2))


### NOT READY YET ###

        # if overall_numbers / 2  < choice_numbers:
        #
        #     half_of_overall_numbers = int(overall_numbers/2)
        #
        #     for j in range(0, half_of_overall_numbers):
        #
        #         AB = self.factor(overall_numbers) / self.factor(choice_numbers) / self.factor(overall_numbers - choice_numbers)
        #
        #         BC = self.factor(choice_numbers) / self.factor(j) / self.factor(choice_numbers - j)
        #
        #         third = self.factor(overall_numbers - choice_numbers) / self.factor(choice_numbers - j) / self.factor((overall_numbers-choice_numbers) -(choice_numbers - j))
        #
        #         ### choice_numbers and good tips  with 2 decimal digits###
        #         print("Your chance to find out exactly", j, "number is 1 to ",round((1/( BC * third / AB)),2))

        # if overall_numbers >=  choice_numbers and overall_numbers/2 >= choice_numbers:
        #
        #     pass





    def lotto_game(self):

        game_overall_numbers = input("how many numbers is the pool?")
        game_choice_numbers = input("how many numbers wanna find out?")

        game_choice_numbers = int(game_choice_numbers)

        list_numbers = []

        for i in range(game_choice_numbers):
             numbers = input("Please give me a number")
             list_numbers.append(numbers)

x = Lotto()

x.lotto_chance()
