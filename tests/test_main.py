import unittest
from TicTacToe.main import Game
#from TicTacToe.Board import Board
from TicTacToe.Player import Player

class GameTests(unittest.TestCase):
    """Tests the game functionality. Do all the other classes work together?"""

    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]

    def setUp(self):
        player1 = Player("Dale", "X")
        player2 = Player()
        self.game = Game(player1, player2)
        #self.board = Board()
        pass

    def test_taketurn(self):
        self.assertTrue(self.game.board.possiblemoves)


    def test_check(self):
        spacestaken = [0, 1, 2]
        #self.assertEqual(self.game.p1.spacestaken, [0,1,2])
        self.assertEqual(set(spacestaken).intersection(GameTests.wins[0]),
                         set(GameTests.wins[0]))

    def TearDown(self):
        self.game.dispose()



if __name__ == '__main__':
    unittest.main()
