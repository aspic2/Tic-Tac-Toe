import unittest
from TicTacToe.Player import Player


class testPlayer(unittest.TestCase):
    """Test the player's interaction with board and evaluation of standing."""

    def test_attributes(self):
        self.assertEqual(Player().winner, False)


class testAI(unittest.TestCase):
    def test_logic(self):
        pass



if __name__ == '__main__':
    unittest.main()
