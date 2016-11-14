# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.

import collections
from operator import itemgetter
from collections import OrderedDict



def anagramm(string1, string2):

    string1= ''.join(string1.split()) # remove all whitespace chars
    string2= ''.join(string2.split()) # remove all whitespace chars

    string1 = string1.lower()
    string2 = string2.lower()

    string1 = sorted(string1)
    string2 = sorted(string2)




    if string1 == string2:
        return True
    else:
        return False

anagramm("alma","mal a")


def count_letters(string3):
    if not isinstance(string3, str):
        raise TypeError("It is not string")
    dict = {}
    for letter in string3:
        if letter not in dict.keys():

            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict
