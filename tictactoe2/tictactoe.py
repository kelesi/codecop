import sys

class Board(object):

    def __init__(self):
        self._init_board()

    def _init_board(self):
        self._board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def set_position(self, player, x, y):
        self._board[y][x] = player

    def get_position(self, x, y):
        return self._board[y][x]

    def _find_row_winner(self, board_representation):
        for row in board_representation:
            if self._has_equal_elements(row):
                return row[0]
        return None

    def _find_column_winner(self):
        transposed_board = map(list, zip(*self._board))
        return self._find_row_winner(transposed_board)

    def _has_equal_elements(self, row):
        row_set = set(row)
        return row_set != set(' ') and len(row_set) == 1

    def _find_diagonal_winner(self):
        board = self._board
        diagonals = [
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]
        return self._find_row_winner(diagonals)

    def get_winner(self):
        winner = self._find_row_winner(self._board)

        if winner is None:
            winner = self._find_column_winner()
        if winner is None:
            winner = self._find_diagonal_winner()

        return winner


class Player(object):

    def __init__(self, mark):
        self._mark = mark

    def __str__(self):
        return self._mark


class TicTacToe(object):
    pass


def main():
    pass


if __name__ == "__main__":
    sys.exit(main())
