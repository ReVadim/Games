from TicTacToe_5.game_settings import EMPTY_SPACE, FIELD_LENGTH, FIELD_WIDTH, INFO, PLAYER_O, PLAYER_X
import random


def get_new_board():
    """ Return player board """
    board = [[EMPTY_SPACE] * FIELD_LENGTH for x in range(FIELD_WIDTH)]

    return board


def display_board(board):
    """ Display game board """

    title = [f'    {x + 1}' for x in range(9)] + [f'   {x + 1}' for x in range(9, FIELD_LENGTH)]
    print(*title, sep='')

    for num, line in enumerate(board):
        print(num + 1, line)


def input_player_letter():
    f""" Choose {PLAYER_X} or {PLAYER_O} letter for playing """

    print(INFO)
    letter = ''
    while not (letter == PLAYER_X or letter == PLAYER_O):
        print(f'Введите символ: {PLAYER_X} или {PLAYER_O} - ')
        letter = input().upper()
    if letter == PLAYER_X:
        return [PLAYER_X, PLAYER_O]
    else:
        return [PLAYER_O, PLAYER_X]


def is_empty_space(board, position_y, position_x):
    """ Check empty space """

    return board[position_y][position_x] == EMPTY_SPACE


def first_player():
    """ Select who goes first """
    if random.randint(0, 1) == 0:
        return 'human'
    else:
        return 'ai'


def player_move(board, letter):
    """ Assign a value in the selected cell  """
    move_y = move_x = False

    while not move_x:
        move_y, *move_x = input("Введите координаты клетки через пробел ").split()
        move_y, move_x = int(move_y) - 1, int(move_x[0]) - 1

        if move_y not in range(FIELD_WIDTH) or move_x not in range(FIELD_LENGTH):
            print(f'Введите корректные данные! Не превышающие {FIELD_LENGTH}х{FIELD_WIDTH}')
            continue
        if board[move_y][move_x] != EMPTY_SPACE:
            print('Ячейка уже занята')
        board_copy = get_board_copy(board)
        if is_empty_space(board_copy, move_y, move_x):
            board_copy[move_y][move_x] = letter

        return board_copy


def get_board_copy(board):
    board_copy = []
    for _ in board:
        board_copy.append(_)
    return board_copy


def random_move(board, letter):
    """ Ai make move """

    print('Ход компьютера')
    y = random.randint(0, FIELD_WIDTH - 1)
    x = random.randint(0, FIELD_LENGTH - 1)

    print('x = ', x, 'y = ', y)
    board_copy = get_board_copy(board)

    if is_empty_space(board_copy, y, x):
        board_copy[y][x] = letter
    else:
        print('Ячейка занята')
    return board_copy


def is_loose(table, letter):

    for y in range(FIELD_WIDTH):
        for x in range(FIELD_LENGTH - 4):
            cell = table[y][x]
            if cell != letter:
                continue
            loose = True
            for i in range(1, 5):

                if table[y][x + i] != letter:
                    loose = False
                    break
            return loose

    for y in range(FIELD_WIDTH - 4):
        for x in range(FIELD_LENGTH):
            cell = table[y][x]
            if cell != letter:
                continue
            loose = True
            for i in range(1, 5):
                if table[y + i][x] != letter:
                    loose = False
                    break
            if loose:
                return True

    for y in range(FIELD_WIDTH - 4):
        for x in range(FIELD_LENGTH - 4):
            cell = table[y][x]
            if cell != letter:
                continue
            loose = True
            for i in range(1, 5):
                if table[y + i][x + i] != cell:
                    loose = False
                    break
            return loose

    for y in range(4, FIELD_WIDTH):
        for x in range(FIELD_LENGTH - 4):
            cell = table[y][x]
            if cell != letter:
                continue
            loose = True
            for i in range(1, 5):
                if table[y - i][x + i] != letter:
                    loose = False
                    break
            if loose:
                return True


def is_board_full(table):
    """ Check empty position """

    for i in range(FIELD_LENGTH):
        for j in range(FIELD_WIDTH):
            if table[i][j] == EMPTY_SPACE:
                return False
    return True
