# TODO: make game board size scalable. Board technically is scalable now
# TODO: (defaults to 3x3, but can be changed)
# TODO: In practice, scalable board is restricted by two things:*
# TODO:     1. print_board formatting
# TODO:     2. Game evaluation (how to keep winning evaluation without writing out all
# TODO:        winning possibilities for each board size)

class Board(object):
    """This class handles displaying and altering the pieces on the board."""
    def __init__(self, rows=3):
        self.gameboard = []
        self.spaces = range(rows**2)
        for space in self.spaces:
            self.gameboard.append(space)
        # possible moves starts as same size as gameboard, then decreases
        # as moves are made. Should be: boardsize - no. of moves played
        self.possiblemoves = self.gameboard[:]
        self.winner = False

    def updateBoard(self, square=5, marker='#'):
        """Method takes a tuple from the player including their desired board
        slot and their marker. Method then confirms that their move is legal.
        If move is legal, the token in the move's slot is popped and given to
        the player. If move is not legal, method returns None and loop in
        main.takeTurn() repeats
        """
        player_marker = marker
        # compensate for 0 indexing
        square = square
        if self.gameboard[square] in self.possiblemoves:
            self.gameboard[square] = marker
            x = self.possiblemoves.index(square)
            # TODO: remove this once zero index correction is re added
            print("Trying to pop possiblemoves", self.possiblemoves[x])
            return self.possiblemoves.pop(x)
        else:
            print("That spot is taken. Please pick another option.\n")


    def print_board(self):
        """Prints the board nicely to the terminal. This will eventually be
        reworked so that it is scalable, since the current layout only works
        for a 3x3 board.
        """
        print("\n")
        print(self.gameboard[0], "|", self.gameboard[1], "|", self.gameboard[2])
        print("--+---+--")
        print(self.gameboard[3], "|", self.gameboard[4], "|", self.gameboard[5])
        print("--+---+--")
        print(self.gameboard[6], "|", self.gameboard[7], "|", self.gameboard[8])
        print("\n")
