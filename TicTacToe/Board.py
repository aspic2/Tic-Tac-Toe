class Board(object):
    def __init__(self, rows=3):
        self.gameboard = []
        self.spaces = range(rows**2)
        for space in self.spaces:
            self.gameboard.append(space)
        self.possiblemoves = self.gameboard[:]
        self.winner = False

    def updateBoard(self, square=5, marker='#'):
        player_marker = marker
        # compensate for 0 indexing
        square = square
        if self.gameboard[square] in self.possiblemoves:
            self.gameboard[square] = marker
            x = self.possiblemoves.index(square)
            print("Trying to pop possiblemoves", self.possiblemoves[x])
            return self.possiblemoves.pop(x)
        else:
            print("That spot is taken. Please pick another option.\n")


    def print_board(self):
        print("\n")
        print(self.gameboard[0], "|", self.gameboard[1], "|", self.gameboard[2])
        print("--+---+--")
        print(self.gameboard[3], "|", self.gameboard[4], "|", self.gameboard[5])
        print("--+---+--")
        print(self.gameboard[6], "|", self.gameboard[7], "|", self.gameboard[8])
        print("\n")
        #return self.gameboard
