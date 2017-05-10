#TODO: still gotta add the AI.

import random
import time


class Player(object):
    """Holds the player's name, marker ('X' or 'O') and spaces taken.
    Spaces taken is used to evaluate the winner.
    """

    def __init__(self, name="AI", marker="O"):
        """Name defaults to 'AI'. Marker defaults to 'O'."""
        self.name = name
        self.marker = marker
        self.spacestaken = []
        self.winner = False

    def makemove(self, openings):
        """Player selects their next move. Move is set to board to fulfill."""
        if self.name == "AI":
            print("AI's turn\n")
            #time.sleep(3)
            square = random.choice(openings)
        else:
            square = input("Make your move:\n> ")
            try:
                square = int(square)
            except ValueError:
                print("Invalid choice. Please enter an available spot.")
                square = self.makemove(openings)
        return square

    def updatespacestaken(self, square):
        """After a move, the player's list of taken spaces is updated and
        evaluated. The winning combination of spaces is kept in the Game
        class, so the player's taken spaces is compared to that.
        """
        self.spacestaken.append(square)


class AI(Player):
    """Still empty, but will eventually contain the minimax logic for the AI
    to evaluate moves.
    """
    pass
