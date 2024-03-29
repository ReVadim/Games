import sys
from Four_In_Arow import settings


def get_new_board():
    """ Return player board """

    board = {}

    for column_index in range(settings.BOARD_WIDTH):
        for row_index in range(settings.BOARD_HEIGHT):
            board[(column_index, row_index)] = settings.EMPTY_SPACE

    return board


def display_board(board):
    """ Display game board """

    tile_chars = []
    for row_index in range(settings.BOARD_HEIGHT):
        for column_index in range(settings.BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])

    print(settings.BOARD.format(*tile_chars))


def ask_for_player_move(player_tile, board):
    """ Choose column on the table """

    while True:
        print(f'Player {player_tile} enter a column or Quit:')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in settings.COLUMN_LABELS:
            print(f'Enter a number from 1 to {settings.BOARD_WIDTH}.')
            continue

        column_index = int(response) - 1

        if board[(column_index, 0)] != settings.EMPTY_SPACE:
            print('That column is full, select another one.')
            continue
        # find empty place
        for row_index in range(settings.BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == settings.EMPTY_SPACE:
                return column_index, row_index


def is_full(board: dict) -> bool:
    """ Return True if not empty places on board """

    for row_index in range(settings.BOARD_HEIGHT):
        for column_index in range(settings.BOARD_WIDTH):
            if board[(column_index, row_index)] == settings.EMPTY_SPACE:
                return False
    return True


def is_winner(player_tile, board):
    """ Check 4 in a row. Return bool """
    # check all board
    for column_index in range(settings.BOARD_WIDTH - 3):
        for row_index in range(settings.BOARD_HEIGHT):
            # find 4 in horizontal
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(settings.BOARD_WIDTH):
        for row_index in range(settings.BOARD_HEIGHT - 3):
            # find 4 in vertical
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(settings.BOARD_WIDTH - 3):
        for row_index in range(settings.BOARD_HEIGHT - 3):
            # find 4 in diagonal
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    return False
