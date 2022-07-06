from TicTacToe_5.service import (
    first_player,
    get_new_board,
    display_board,
    input_player_letter,
    random_move,
    player_move,
    is_loose,
    is_board_full,)


def main():
    """ Main function """

    array = get_new_board()
    human_letter, ai_letter = input_player_letter()
    game_is_playing = True
    player = first_player()

    while game_is_playing:
        if player == 'human':
            print('Ваш ход: ')
            display_board(array)
            player_move(array, human_letter)
            display_board(array)

            if is_loose(array, human_letter):
                print('Ты проиграл')
                game_is_playing = False
            else:
                if is_board_full(array):
                    print('Ничья!')
                    break
                else:
                    player = 'ai'

        else:
            random_move(array, ai_letter)
            if is_loose(array, ai_letter):
                print('Вы выиграли!')
                game_is_playing = False
            else:
                if is_board_full(array):
                    print('Ничья!')
                    break
                else:
                    player = 'human'


if __name__ == '__main__':
    main()
