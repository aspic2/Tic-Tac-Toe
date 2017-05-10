#Classic 3x3 game of Tic-Tac-Toe against the computer


from TicTacToe.Board import Board
from TicTacToe.Player import Player
from sys import exit


class Game(object):
    """The brains. Brings all other classes together and runs the game.
    """

    """This variable needs to be refactored to be scalable. Also, it may need
    to be moved to a different place.
    """
    winning_spaces = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
                        [0,4,8], [2,4,6]]

    def __init__(self, player1, player2):
        """Initialize the game with board and two players, one of which is AI"""
        self.board = Board()
        self.p1 = player1
        self.p2 = player2
        self.winner = None
        self.over = False

    def check(self, player):
        """Method checks if a player has won the game and if there are still
         available moves.
         """
        for row in Game.winning_spaces:
            if set(player.spacestaken).intersection(row) == set(row):
                self.winner = player
                return True
        if not self.board.possiblemoves:
            return True
        else:
            return False

    def taketurn(self, player):
        """Method holds logic for each player's full turn. It returns False
        (the value of Game.check() as long as a player has not yet won and
        there are still moves available.
        """
        while self.board.possiblemoves:
            space = None
            # odd syntax here because space = 0 evaluates to not space,
            #  giving a player 2 turns in one if they select 0.
            while space is None:
                self.board.print_board()
                move = player.makemove(self.board.possiblemoves)
                space = self.board.updateBoard(move, player.marker)
            print("\nHere is the popped token:")
            print(space)
            print("\nSpaces still available: ")
            print(self.board.possiblemoves)
            player.updatespacestaken(space)
            print("\n%s's taken spots:" % player.name)
            print(player.spacestaken)
            return self.check(player)
        else:
            return True

    def play(self):
        """Logic connecting each player's turn into one round."""
        # TODO: bring while loop from main() back to Game class.
        self.over = self.taketurn(self.p1)
        if self.over:
            if self.winner:
                print("\n%s has won the game." % self.winner.name)
            else:
                print("\nThat was a tie game.")
        else:
            self.over = self.taketurn(self.p2)
            if self.over:
                if self.winner:
                    print("\n%s has won the game." % self.winner.name)
                else:
                    print("\nThat was a tie game.")

######################################################################


def main():
    """Prints a nice intro, then initializes players and starts game."""
    print("-" * 50)
    print("Welcome to Tic-Tac-Toe!")
    name = input("\nWhat is your name?\n> ")
    print("Hello, %s. You will be playing against your computer." % name)

    marker = input("Would you like to be X or O?\n> ").upper()
    if marker != 'X' and marker != 'O':
        print("That is not a valid choice. Defaulting to X")
        marker = 'X'
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

    #person = Player('Human','X')
    #AI = Player()
    #game = Game(person, AI)
    while not game.over:
        game.play()






if __name__ == '__main__':
    main()
