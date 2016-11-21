import model_todo
import view_todo

class Controller:

    def __init__(self):
        self.View = view_todo.View()
        self.Process = model_todo.Process()



x = Controller()

x.Process.add_people()
x.Process.add_people()
x.View.View_in_screen()
