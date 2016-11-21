import model_hangman
import view_hangman


class Controller:

     def __init__(self):
         self.View = view_hangman.View()
         self.Hangman = model_hangman.Hangman()
