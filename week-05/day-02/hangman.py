### IMPORT MODULES ###

from random_words import RandomWords


##### HANGMAN ####



class Hangman:

    Guess_WORD = []
    guesses = 0

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
        self.Guess_WORD_IN_LIST = list(self.Guess_WORD)
        while self.Guess_WORD != self.word:
            self.guess_letter = input("Guess a word!\n")
            for i in range (len(self.word)):
                if self.word[i] == self.guess_letter:
                    self.Guess_WORD[i] = self.guess_letter
                    print(self.Guess_WORD)
                    self.guesses += 1
                    self.hangman_graphic()
                if self.word[i] not in self.word:
                    self.bad_guuesses += 1
        print("YOU FIND OUT THE WORD. YOU ARE THE MASTER. YOUR TIPS WAS",self.guesses)
        self.before_the_game()

    ### PICTURE ###

    def hangman_graphic(self):
        if self.guesses == 0:
            print( "________      ")
            print( "|      |      ")
            print( "|             ")
            print( "|             ")
            print( "|             ")
            print( "|             ")
        elif self.guesses == 1:
            print( "|      0      ")
            print( "________      ")
            print( "|             ")
            print( "|             ")
            print( "|      |      ")
            print( "|             ")
        elif self.guesses == 2:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /       ")
            print( "|             ")
            print( "|             ")
        elif self.guesses == 3:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|      ")
            print( "|             ")
            print( "|             ")
        elif self.guesses == 4:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|\     ")
            print( "|             ")
            print( "|             ")
        elif self.guesses == 5:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|\     ")
            print( "|     /       ")
            print( "|             ")
        else:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|\     ")
            print( "|     / \     ")
            print( "|             ")
            print( "GAME OVER!")

# CALL THE GAME ###

x = Hangman()
x.before_the_game()
