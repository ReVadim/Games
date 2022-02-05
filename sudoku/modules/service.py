import random


def get_puzzle():
    """ Choosing one puzzle from the collection """
    with open('resources/sudokupuzzles.txt') as puzzle_stock:
        puzzles = puzzle_stock.readlines()

    for i, puzzle in enumerate(puzzles):
        puzzles[i] = puzzle.strip()

    puzzle = random.choice(puzzles)
    return puzzle
