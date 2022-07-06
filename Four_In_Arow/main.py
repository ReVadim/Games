import sys

from Four_In_Arow import service
from Four_In_Arow import settings


assert len(settings.COLUMN_LABELS) == settings.BOARD_WIDTH


def main():
    print(settings.HELLO)
    # start new game
    game_board = service.get_new_board()
    player_turn = settings.PLAYER_X

    while True:
        service.display_board(game_board)
        player_move = service.ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if service.is_winner(player_turn, game_board):
            service.display_board(game_board)
            print(f'Player {player_turn} has won!')
            sys.exit()
        elif service.is_full(game_board):
            service.display_board(game_board)
            print('There is a tie!')
            sys.exit()

        # next player move
        if player_turn == settings.PLAYER_X:
            player_turn = settings.PLAYER_O
        elif player_turn == settings.PLAYER_O:
            player_turn = settings.PLAYER_X


if __name__ == '__main__':
    main()
