class View:

    bad_guesses = 0

        ### PICTURE ###
    def hangman_graphic(self):
        if self.bad_guesses == 0:
            print( "________      ")
            print( "|      |      ")
            print( "|             ")
            print( "|             ")
            print( "|             ")
            print( "|             ")
        elif self.bad_guesses == 1:
            print( "|      0      ")
            print( "________      ")
            print( "|             ")
            print( "|             ")
            print( "|      |      ")
            print( "|             ")
        elif self.bad_guesses == 2:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /       ")
            print( "|             ")
            print( "|             ")
        elif self.bad_guesses == 3:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|      ")
            print( "|             ")
            print( "|             ")
        elif self.bad_guesses == 4:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|     /|\     ")
            print( "|             ")
            print( "|             ")
        elif self.bad_guesses == 5:
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

x = View()
x.hangman_graphic()
