#Handles assembly, display, and updates to the gameboard

class Board(object):
    def __init__(self, dimensions=3):
        self.dimensions = dimensions
        self.board = []
        self.row = []
        space = "M"
        for x in range(dimensions):
            self.row.append(space)
        for row in range(dimensions):
            self.board.append(self.row)

    def display(self):
        self.displayboard = self.board
        row_divider = "-"
        for row in range(self.dimensions):
            self.displayboard.append(row_divider)        
        for row in self.board:
            for space in row:
                print(space, end='')
            print('')


b = Board()

b.display()
