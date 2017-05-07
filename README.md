# TicTacToe
Game of Tic-Tac-Toe against the computer (currently not working)
Prints a game grid to your command line where you take turns playing against
your computer until one of you wins or the board fills up.

## How To Play
*TODO: Game evaluation is currently not working, so the game will continue
until the board fills up and will be called a stalemate.*

0 | 1 | 2
--+---+--
3 | 4 | 5
--+---+--
6 | 7 | 8

The game begins by asking for your player name (defaults to PLAYER) and your
chosen marker (defaults to X).
Next the board is built and gameplay begins.

*TODO: make game board size scalable. Board technically is scalable now
TODO: (defaults to 3x3, but can be changed)
TODO: In practice, scalable board is restricted by two things:
1. print_board formatting
2. Game evaluation (how to keep winning evaluation without writing out all
  winning possibilities for each board size)*

Each round you will see a printout of the board. Put in the number for the
square where you would like to move, and your token will replace the current
occupant.

*TODO: Update process for selecting already occupied squares.
Game currently skips turn if you put in an index that has already been taken.*


## Requirements
TicTacToe is written in Python 3. No other packages or extensions needed!


## LICENSE
TicTacToe is under the MIT license.
