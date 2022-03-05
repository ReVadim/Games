import sys

from service import get_new_board, display_board, ask_for_player_move
from . import settings


assert len(settings.COLUMN_LABELS) == settings.BOARD_WIDTH


def main():
    print(settings.HELLO)
    # start new game
    game_board = get_new_board()
    player_turn = settings.PLAYER_X

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if is_winner(player_turn, game_board):
            display_board(game_board)
            print(f'Player {player_turn} has won!')
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print('There is a tie!')
            sys.exit()

        # next player move
        if player_turn == settings.PLAYER_X:
            player_turn = settings.PLAYER_O
        elif player_turn == settings.PLAYER_O:
            player_turn = settings.PLAYER_X


