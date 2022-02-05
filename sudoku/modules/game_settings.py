EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH

INFO = """
       Sudoku Puzzle, by ReVadim.
       
       Sudoku is a number placement logic puzzle game.
       A Sudoku grid is a 9x9 grid of numbers.
       Try to place numbers in the grid such that every row,
       column, and 3x3 box has the numbers 1 through 9 once and only once.
       
       For example:
       
       5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
       6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
       . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
       ------+-------+------     ------+-------+------
       8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
       4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
       7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
       ------+-------+------     ------+-------+------
       . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
       . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
       . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9  
       """

CONGRATULATIONS = """
    Congratulations! You solved the puzzle!
    Thanks for playing!
    """

RULES = """
    Enter a move, or (R)ESET, (N)EW, (U)NDO, (O)RIGINAL, INFO or (Q)UIT:
    (For example, a move looks like "B4 9".)
    """

WARNING = """
    You cannot overwrite the original grid numbers.
    Enter ORIGINAL to view the original grid.
    """
