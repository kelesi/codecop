import unittest
from parameterized import parameterized
from mock import patch, MagicMock

from tictactoe import Board

class TestTicTacToe(unittest.TestCase):

    def _new_board_of(self, board_representation):
        board = Board()
        for y in xrange(len(board_representation)):
            for x in xrange(len(board_representation[y])):
                board.set_position(board_representation[y][x], x, y)
        return board

    def test_set_position(self):
        board = Board()
        board.set_position('x', 1, 2)  # mutating
        expected = 'x'
        self.assertEqual(expected, board.get_position(1, 2))

    def test_first_row_win(self):
        board = Board()
        player = 'x'
        board.set_position(player, 0, 0)
        board.set_position(player, 1, 0)
        board.set_position(player, 2, 0)
        self.assertEqual(player, board.get_winner())

    def test_winner_on_empty_board(self):
        board = Board()
        self.assertEqual(None, board.get_winner())

    def test_row_winner(self):
        board = self._new_board_of([
            [' ', ' ', ' '],
            ['x', 'x', 'x'],
            [' ', ' ', ' ']
        ])
        self.assertEqual('x', board.get_winner())

    def test_column_winner(self):
        board = self._new_board_of([
            [' ', 'x', ' '],
            [' ', 'x', ' '],
            [' ', 'x', ' ']
        ])
        self.assertEqual('x', board.get_winner())

    def test_primary_diagonal_winner(self):
        board = self._new_board_of([
            ['x', ' ', ' '],
            [' ', 'x', ' '],
            [' ', ' ', 'x']
        ])
        self.assertEqual('x', board.get_winner())


    def test_secondary_diagonal_winner(self):
        board = self._new_board_of([
            [' ', ' ', 'x'],
            [' ', 'x', ' '],
            ['x', ' ', ' ']
        ])
        self.assertEqual('x', board.get_winner())