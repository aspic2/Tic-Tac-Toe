#Command line tic tac toe
'''
Analysis and Design:
  App must be able to:
      1) Render board (3x3) on screen with placed markers
      2) Allow user to input commands to place markers
      3) Have AI place markers, alternating with user
      4) Keep score over multiple games


Use Case:
    Play tic-tac-toe
    User on command line
    1. User runs script from command line, specifying no. of rounds to play
    2. Game initializes, board is assembled and printed
    3. User is asked to pick a turn, either first (x) or second (o)
    4. First player places marker (X) in desired spot.
        Spot is removed as playable area
    5. Second player (AI) does same with available spots.
    6. Players continue alternating play until one gets 3-in-a-row or all spots are occupied.
    7. Game score is presented.

User Story
    As a Tic-Tac-Toe player,
    I want an AI system to play against
    So that I can improve my logic skills

Player
    Command line inputs

Nouns:
    Player
    No. of rounds
    board
    game
    markers
    AI (Player2)
    Score


AI


Board
    3x3 board
    Mutable with symbols (Players' Chosen Initial (e.g. "M"))


Scoring:

    1 pt per mark on screen
    3 pts for three in row

Things currently not working:
show available spaces


'''


class Board(object):
    def __init__(self, rows):
        self.gameboard = []
        self.spaces = rows ** 2
        self.possiblemoves = []
        for row in range(self.spaces):
            self.gameboard.append("_")

    def getSpace(self, space):
        print(self.gameboard[space])

    #does not work
    def showOpenSpaces(self):
        self.possiblemoves = []
        for x in range(self.spaces):
            if self.gameboard[x] == "_":
                self.possiblemoves.append(x)
        return self.possiblemoves

    def updateBoard(self, square):
        self.gameboard[square] = "M"
        return self.gameboard

    def print_board(self):
        print("\n")
        print(self.gameboard[0], "|", self.gameboard[1], "|", self.gameboard[2])
        print("--+---+--")
        print(self.gameboard[3], "|", self.gameboard[4], "|", self.gameboard[5])
        print("--+---+--")
        print(self.gameboard[6], "|", self.gameboard[7], "|", self.gameboard[8])
        print("\n")
        #return self.gameboard


class Player(object):
    score = 0
    mark = 'X'


    def makeMove(self):
        #move = input("Place your marker:\n[xcoordinate], [ycoord]")
        row = input("Guess the row:")
        try:
            row = int(row)
        except TypeError as e:
            print('please enter an integer on the board')
            makeMove(self)
        column = input("Guess the column:")
        try:
            column = int(column)
        except TypeError as e:
            print('please enter an integer on the board')
            makeMove(self)
        return row, column

class AI(Player):

    def randomMove():
        pass


class Gameplay(object):
    rounds = 5
    #use a modulo to alternate turns




b = Board(3)
b.print_board()
b.updateBoard(1)
b.print_board()
b.getSpace(1)
b.getSpace(0)

print(b.showOpenSpaces())



#print(type(tictactoe.gameboard))
