### IMPORT MODULES ###

from random_words import RandomWords
import os

##### HANGMAN ####



class Hangman:

    Guess_WORD = []
    guesses = 0
    bad_guesses = 0
    used_letters = []

### BASIC DATA ###




#### BEFORE THE GAME ###

    def before_the_game(self):
        answer = input("Do you wanna play with me? (YES/NO)\n")
        if answer == "NO":
            print("PLEASE")
            self.before_the_game()
        elif answer == "YES":
            self.start_the_game()
        else:
            print("Please answer with YES or NO")

    ### START THE GAME ###

    def start_the_game(self):

        ### GENERATE A WORD ###
        rw = RandomWords()
        generate_word = rw.random_word()
        self.word = generate_word

        ### GENERATE SAME A SAME LONG STRING IN LIST ###
        for i in range(len(self.word)):
            self.Guess_WORD.append("-")
        print(self.word)
        self.word = list(self.word)
        print(self.Guess_WORD)
        self.find_out_the_word()
    ## FIND OUT THE WORD ###

    def find_out_the_word(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.Guess_WORD_IN_LIST = list(self.Guess_WORD)
        while self.Guess_WORD != self.word:
            self.guess_letter = input("Guess a word!\n")
            self.used_letters.append(self.guess_letter)
            for i in range (len(self.word)):
                if self.word[i] == self.guess_letter:
                    self.Guess_WORD[i] = self.guess_letter
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.Guess_WORD)
                    self.guesses += 1
                    print("used letter:",self.used_letters)
                    # self.hangman_graphic()

        print("YOU FIND OUT THE WORD. YOU ARE THE MASTER. YOUR TIPS WAS",self.guesses)
        self.Guess_WORD = []
        self.word = []
        self.before_the_game()


# CALL THE GAME ###

# x = Hangman()
# x.before_the_game()
