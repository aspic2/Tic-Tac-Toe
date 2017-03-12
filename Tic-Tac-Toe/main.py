#Classic 3x3 game of Tic-Tac-Toe against the computer


'''errors:
1) Game.check method is not properly evaluating winning positions.
2) Handle invalid input
3) Compensate for 0 indexing: make spaces 1 - 9

'''

from Board import Board
from Player import Player
from sys import exit

class Game(object):

    winning_spaces = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]]


    def __init__(self, player1, player2):
        self.board = Board()
        self.p1 = player1
        self.p2 = player2
        self.haswon = ()
        self.over = False

    def check(self, player):
        for row in Game.winning_spaces:
            if row in player.spacestaken:
                self.haswon.append(player.name)
                return True
        if not self.board.possiblemoves:
            return True
        else:
            return False


    def taketurn(self, player):
        while self.board.possiblemoves:
            self.board.print_board()
            move = player.makeMove(self.board.possiblemoves)
            space = self.board.updateBoard(move, player.marker)
            print("\nHere is the popped token:")
            print(space)
            print("\nSpaces still available: ")
            print(self.board.possiblemoves)
            player.updatespacestaken(space)
            print("\nPlayer's taken spots:")
            print(player.spacestaken)
            return self.check(player)
        else:
            return True



    def play(self):
        while self.over == False:
            self.over = self.taketurn(self.p1)
            self.over = self.taketurn(self.p2)
        else:
            if self.haswon:
                print("\n%s has won the game." % self.haswon)
            else:
                print("\nThat was a tie game.")


######################################################################


def main():
    '''print("-" * 50)
    print("Welcome to Tic-Tac-Toe!")
    name = input("\nWhat is your name?\n> ")
    print("Hello, %s. You will be playing against your computer." % name)

    marker = input("Would you like to be X or O?\n> ").upper()
    if marker != 'X' and marker != 'O':
        print("That is not a valid choice. Defaulting to X")
    else:
        print("%s is an Excellent choice, %s. Initializing your game now."
            % (marker, name))
    player = Player(name, marker)

    print("Initializing AI...")
    if marker == "O":
        AI = Player(marker='X')
        game = Game(AI, player)
    else:
        AI = Player()
        game = Game(player, AI)
    '''
    person = Player('Test','X')
    AI = Player()
    game = Game(person, AI)
    game.play()



if __name__ == '__main__':
    main()
