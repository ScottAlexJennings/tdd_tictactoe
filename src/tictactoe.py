class TicTacToe:

    grid_dict = {1: (0, 0), 2: (1, 0), 3: (2, 0), 
                 4: (0, 1), 5: (1, 1), 6: (2, 1), 
                 7: (0, 2), 8: (1, 2), 9: (2, 2)}

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display_board(self):
        for row in self.board:
            print(' | '.join(row))

    def make_move(self, inp):

        inp = int(inp)

        x, y = self.grid_dict[inp]

        if self.board[y][x] == ' ':
            self.board[y][x] = 'X'
        else:
            print("Spot already taken!")




if __name__ == '__main__':
    game = TicTacToe()
    print("Grid format: \n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    while True:
        inp = input("Make a move (1 - 9): ")

        if inp.isdigit() and int(inp) in range(1, 10):
            break
        else:
            print("Invalid value. Try again.")
            
    game.make_move(inp)

    game.display_board()


    
