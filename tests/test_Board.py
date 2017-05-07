import unittest
from TicTacToe.Board import Board


class TestBoard(unittest.TestCase):
    """This module confirms that the board prints and interacts properly"""
    def test_Board(self):
        self.assertEqual(Board().gameboard, Board(3).gameboard)


if __name__ == '__main__':
    unittest.main()
