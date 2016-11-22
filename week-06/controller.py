from view import View
import map_of_game
import character


class Control:
    def __init__(self):
        self.map = map_of_game.Game_Map()
        self.view = View()

        self.view.display_map(self.map.board)
        

    def draw_game_map(self):
        self.view.root.mainloop()




x = Control()

x.draw_game_map()
