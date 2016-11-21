# Create a class the displays the Elevator art and navigation (list of commands)


### PICTURE ###

class View:

    def __init__(self,all_levels,current_level,people):
        self.current_level = current_level
        self.all_levels = all_levels
        self.people = people

    def Picture(self,all_levels,current_level,people):

        if current_level == 0:

            print(" ___________________________________")
            print(" `._______________________________.'")

            for i in range(all_levels-1):
                print("     || ||       || ||       || ||")


            print("     || || [",people,"] || ||       ||_||")


        else:

            print("____________________________________")
            print("`.________________________________.'")


            for i in range (1,all_levels):
                if all_levels - i == current_level:
                    print("  || || [",people,"] || ||        || ||")
                else:
                    print("  || ||       || ||        || ||")

            print(" _||_||_______||_||________||_||_")
            print("___________________________________")


### CALL THE FUNCTIONS ###

# x = View(7,10,4)
#
# x.Picture()
