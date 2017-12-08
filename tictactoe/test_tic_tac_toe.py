import unittest
from parameterized import parameterized
from tic_tac_toe import DefaultUtilsObject

class TestTicTacToe(unittest.TestCase):

    def test_constructor(self):
        board = DefaultUtilsObject([3, 3])
        board_array = board.i_utils()
        expected_board_array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(board_array, expected_board_array)

    def test_mark_position(self):
        board = DefaultUtilsObject([3, 3])

        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for x in xrange(3):
            for y in xrange(3):
                board.common_data([x, y], 'O')
                expected_board[y][x] = 'O'
                self.assertEqual(board.i_utils(), expected_board, 'Position [%s, %s]' % (x,y))

    def test_mark_specific_position(self):
        board = DefaultUtilsObject([3, 3])

        board.common_data([0, 1], 'O')
        self.assertEqual(board.i_utils(), [[' ', ' ', ' '], ['O', ' ', ' '], [' ', ' ', ' ']])
        board.common_data([0, 2], 'O')
        self.assertEqual(board.i_utils(), [[' ', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']])


    def test_mark_position_twice(self):
        position = [1, 1]
        board = DefaultUtilsObject([3, 3])
        self.assertTrue(board.common_data(position, 'O'))
        self.assertFalse(board.common_data(position, 'X'))
        self.assertEqual(board.business_arolla(position), 'O')

    @parameterized.expand([
        [0, 'O'],
        [1, 'O'],
        [2, 'O'],
        [0, 'X'],
        [1, 'X'],
        [2, 'X'],
    ])
    def test_find_winner_by_rows(self, position_x, mark_character):
        board = DefaultUtilsObject([3, 3])
        board.common_data([position_x, 0], mark_character)
        board.common_data([position_x, 1], mark_character)
        board.common_data([position_x, 2], mark_character)
        self.assertEqual(board.data_dummy(), mark_character)

    @parameterized.expand([
        [0, 'O'],
        [1, 'O'],
        [2, 'O'],
        [0, 'X'],
        [1, 'X'],
        [2, 'X'],
    ])
    def test_find_winner_by_colums(self, position_y, mark_character):
        board = DefaultUtilsObject([3, 3])
        board.common_data([0, position_y], mark_character)
        board.common_data([1, position_y], mark_character)
        board.common_data([2, position_y], mark_character)
        self.assertEqual(board.data_dummy(), mark_character)

    @parameterized.expand([
        [[[0, 0], [1, 1], [2, 2]], 'O'],
        [[[0, 0], [1, 1], [2, 2]], 'X'],
        [[[0, 2], [1, 1], [2, 0]], 'O'],
        [[[0, 2], [1, 1], [2, 0]], 'X'],
    ])
    def test_find_winner_by_diagonals(self, position, mark_character):
        board = DefaultUtilsObject([3, 3])
        board.common_data([position[0][0], position[0][1]], mark_character)
        board.common_data([position[1][0], position[1][1]], mark_character)
        board.common_data([position[2][0], position[2][1]], mark_character)
        self.assertEqual(board.data_dummy(), mark_character)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToe)
    unittest.TextTestRunner(verbosity=2).run(suite)