import random
import time


class Player(object):


    def __init__(self, name="AI", marker="O"):
        self.name = name
        self.marker = marker
        self.spacestaken = []
        self.winner = False

    def makemove(self, openings):
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
        self.spacestaken.append(square)


class AI(Player):
    pass
