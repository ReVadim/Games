import sys
import service
from game_settings import RULES, MONEY, LOOSE


def main():
    """ main function """
    print(RULES)
    money = MONEY
    while True:
        if money <= 0:
            print(LOOSE)
            sys.exit()

        print('Money: ', money)
        bet = service.get_bet(money)
        deck = service.get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        print('Bet: ', bet)

        while True:
            service.display_hands(player_hand, dealer_hand, False)
            print()

            if service.get_hand_value(player_hand) > 21:
                break

            move = service.get_move(player_hand, money - bet)

            if move == 'D':
                additional_bet = service.get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print('Bet increased to {}.'.format(bet))
                print('Bet: ', bet)

            if move == 'H':
                new_card = deck.pop()
                rank, suit = new_card
                print('You drew a {} of {}.'.format(rank, suit))
                player_hand.append(new_card)

                if service.get_hand_value(player_hand) > 21:
                    continue
            if move in ('S', 'D'):
                break

        if service.get_hand_value(player_hand) < 21:
            while service.get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                service.display_hands(player_hand, dealer_hand, False)

                if service.get_hand_value(dealer_hand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        service.display_hands(player_hand, dealer_hand, True)

        player_value = service.get_hand_value(player_hand)
        dealer_value = service.get_hand_value(dealer_hand)

        if dealer_value > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${}!'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


if __name__ == '__main__':
    main()
