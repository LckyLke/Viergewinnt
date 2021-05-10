from player import Player
class Viergewinnt():
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]

    def print_board(self):
        for row in self.board:
            for i,field in enumerate(row):
                if i == len(row) - 1:
                    print(f'|{field}|', end="")
                    continue
                print(f'|{field}', end="")
            print()
        print("-"*15)
        print('|0|1|2|3|4|5|6|')

    def check_moves(self):
        arr = []
        for y in range(7):
            for row in self.board:
                if row[y] == ' ':
                    arr.append(y)
        reArr = [(y, arr.count(y)) for y in sorted(set(arr))]
        return reArr
    def update_board(self, player, pos):
        pos_moves = self.check_moves()
        for tup in pos_moves:
            if tup[0] == pos:
                to_update_tup = tup
                break
        print("should be placed")
        self.board[to_update_tup[1] - 1][to_update_tup[0]] = player.char
    def check_win(self, p1, p2):
        for row in self.board:
            for y in range(len(row) - 3):
                if row[y] == row[y+1] == row[y+2] == row[y+3] == p1.char:
                    return p1
                if row[y] == row[y + 1] == row[y + 2] == row[y + 3] == p2.char:
                    return p2
        for i in range(7):
            col = [row[i] for row in self.board]

            for y in range(len(col) - 3):
                if col[y] == col[y+1] == col[y+2] == col[y+3] == p1.char:
                    return p1
                if col[y] == col[y+1] == col[y+2] == col[y+3] == p2.char:
                    return p2
        leftrightdig = []

def play(rounds=1):
    p1 = Player(input("Enter a Char for your Player"))
    p2 = Player(input("Enter a Char for your Player2"))
    game = Viergewinnt()
    while True:
        game.print_board()
        p1.set_move(game)
        game.print_board()
        if game.check_win(p1,p2):
            print(f'Player {game.check_win(p1,p2).char} won the game!')
            break
        p2.set_move(game)
        if game.check_win(p1,p2):
            print(f'Player {game.check_win(p1,p2).char} won the game!')
            break

play()