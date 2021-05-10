class Player():
    def __init__(self, char):
        self.char = char

    def set_move(self,game):
        try:
            entVal = int(input("Enter a Column where you want to place:)"))
        except ValueError:
            print("Enter a number")
            return self.set_move(game)
        except Exception:
            print("Unexpected Error")
            return self.set_move(game)
        if entVal in [game.check_moves()[y][0] for y in range(len(game.check_moves()))]:
            game.update_board(self,entVal)
            return

        print('Your number has to be between 0 and 6 and the Column cant be full')
        return self.set_move(game)

