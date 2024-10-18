import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_board_initialization(self):
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board, "The board should initialize as a 3x3 grid of empty strings")
        print("test_board:initialization passed")

    def test_board_move(self):
        game = TicTacToe()
        game.make_move(6)
        expected_board = [[' ', ' ', ' '], [' ', '1', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board, "The first move of the game should have been made")
        print("test_board:make move passed")

if __name__ == '__main__':
    unittest.main()
