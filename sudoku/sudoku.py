import copy
import sys

from modules.game_settings import GRID_LENGTH, EMPTY_SPACE, FULL_GRID_SIZE, BOX_LENGTH, CONGRATULATIONS, RULES, INFO, \
    WARNING
from modules.service import get_puzzle


class SudokuGrid:
    """ Main game class """

    def __init__(self, original_puzzle):
        self.original_puzzle = original_puzzle
        self.grid = {}
        self.reset_grid()  # sets the field to its initial state
        self.moves = []

    def reset_grid(self):
        """ restoring the state of the field tracked in self.grid to self.original_puzzle """

        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE
        assert len(self.original_puzzle) == FULL_GRID_SIZE
        i = 0  # iterates through values from 0 to 80
        y = 0  # iterates through values from 0 to 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.original_puzzle[i]
                i += 1
            y += 1

    def make_move(self, column, row, number):
        """ Put a digit in a column (letter from 'A' to 'I') and a row (digit from 1 to 9) in the field"""

        x = 'ABCDEFGHI'.find(column)  # convert to digit
        y = int(row) - 1

        if self.original_puzzle[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number  # put digit to the field
        self.moves.append(copy.copy(self.grid))  # copy for undo()
        return True

    def undo(self):
        """ Modify field to previous state from self.moves """

        if not self.moves:
            return
        self.moves.pop()

        if not self.moves:
            self.reset_grid()
        else:
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """ Displaying the current state of the field on the screen """

        print('    A B C   D E F   G H I  ')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    print(str(y + 1) + '|  ', end='')

                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    print('| ', end='')  # Displaying vertical line
            print()

            if y == 2 or y == 5:
                print('    ------+-------+------')

    @staticmethod
    def _is_complete_set_of_numbers(numbers):
        """ Return 'True' if numbers contains digits from 1 to 9 """

        return sorted(numbers) == list('123456789')

    def is_solved(self):
        """ Return 'True' if еру field is in a ready state """
        for row in range(GRID_LENGTH):
            row_numbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                row_numbers.append(number)
            if not self._is_complete_set_of_numbers(row_numbers):
                return False

        for column in range(GRID_LENGTH):
            column_numbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                column_numbers.append(number)
            if not self._is_complete_set_of_numbers(column_numbers):
                return False

            for box_x in (0, 3, 6):
                for box_y in (0, 3, 6):
                    box_numbers = []
                    for x in range(BOX_LENGTH):
                        for y in range(BOX_LENGTH):
                            number = self.grid[(box_x + x, box_y + y)]
                            box_numbers.append(number)
                    if not self._is_complete_set_of_numbers(box_numbers):
                        return False
            return True


input("Press Enter to begin...")

puzzle = get_puzzle()

grid = SudokuGrid(puzzle)

while True:
    grid.display()

    if grid.is_solved():  # check if the puzzle is solved
        print(CONGRATULATIONS)
        sys.exit()

    while True:
        print()
        print(RULES)

        action = input('> ').upper().strip()

        if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q') or action == 'INFO':
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                print('Something went wrong, try again')
                continue
            if number.isdigit() is False:
                print('The number is not a digit, try again')
                continue

            column, row = space
            if column not in list('ABCDEFGHI'):
                print('There is no column ', column)
                continue
            if not row.isdigit() or not (1 <= int(row) <= 9):
                print('There is no row ', row)
                continue
            if not (1 <= int(number) <= 9):
                print('Select a number from 1 to 9, not ', number)
                continue
            break

    print()

    if action.startswith('INFO'):
        print(INFO)
        print()
        input('Press "Enter" to continue...')

    if action.startswith('R'):
        grid.reset_grid()
        continue

    if action.startswith('N'):
        grid = SudokuGrid(get_puzzle())
        continue

    if action.startswith('U'):
        grid.undo()
        continue

    if action.startswith('O'):
        original_grid = SudokuGrid(grid.original_puzzle)
        print('The original grid looked like this: ')
        original_grid.display()
        input('Press "Enter" to continue...')

    if action.startswith('Q'):
        print('Thanks for playing!')
        sys.exit()
    try:
        if grid.make_move(column, row, number) is False:
            print(WARNING)
            input('Press "Enter" to continue...')
    except NameError:
        continue
