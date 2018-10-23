"""
### Problem ###

https://leetcode.com/problems/valid-tic-tac-toe/description/

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this
board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

- Players take turns placing characters into empty squares (" ").
- The first player always places "X" characters, while the second player always places "O" characters.
- "X" and "O" characters are always placed into empty squares, never filled ones.
- The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Example 1:

Input: board = ["O  ", "   ", "   "]
Output: false

Explanation: The first player always plays "X".

Example 2:

Input: board = ["XOX", " X ", "   "]
Output: false

Explanation: Players take turns making moves.

Example 3:

Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:

Input: board = ["XOX", "O O", "XOX"]

Output: true

Note:

board is a length-3 array of strings, where each string board[i] has length 3.

Each board[i][j] is a character in the set {" ", "X", "O"}.

"""

import unittest


class TicTacToeTest(unittest.TestCase):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        board_list = list("".join(board))

        num_X = len(list(filter(lambda x: x == "X", board_list)))
        num_O = len(list(filter(lambda x: x == "O", board_list)))

        tic_tac_toes = [
            board[0],  # vertical
            board[1],
            board[2],
            board[0][0] + board[1][0] + board[2][0],  # horizontal
            board[0][1] + board[1][1] + board[2][1],
            board[0][2] + board[1][2] + board[2][2],
            board[0][0] + board[1][1] + board[2][2],  # diagonal
            board[0][2] + board[1][1] + board[2][0]
        ]

        num_X_wins = len(list(filter(lambda x: x == "XXX", tic_tac_toes)))
        num_O_wins = len(list(filter(lambda x: x == "OOO", tic_tac_toes)))

        # blank board
        if num_X == 0 and num_O == 0:
            return True

        # num X must either equal to num Os or num O-1
        if (num_X != num_O) and (num_X != (num_O + 1)):
            return False

        # both players cannot win
        if num_X_wins > 0 and num_O_wins > 0:
            return False

        # for X to win, must have more
        if num_X_wins > 0 and num_X <= num_O: return False

        # for O to win, must have equal X
        if num_O_wins > 0 and num_O != num_X: return False

        return True

    def test_basic(self):
        self.assertEqual(False, self.validTicTacToe(["O  ", "   ", "   "]))
        self.assertEqual(True, self.validTicTacToe(["   ", "   ", "   "]))
        self.assertEqual(False, self.validTicTacToe(["XOX", " X ", "   "]))
        self.assertEqual(False, self.validTicTacToe(["XXX", "OOO", "   "]))
        self.assertEqual(True, self.validTicTacToe(["XOX", "O O", "XOX"]))
        self.assertEqual(False, self.validTicTacToe(["XXX", "XOO", "OO "]))
        self.assertEqual(True, self.validTicTacToe(["XXX", "OOX", "OOX"]))
        self.assertEqual(False, self.validTicTacToe(["OXX", "XOX", "OXO"]))
        self.assertEqual(False, self.validTicTacToe(["XXO", "XOX", "OXO"]))
