import sys
import random
from game_settings import CARDS, BACKSIDE


def get_bet(max_bet: int) -> int:
    """
    Ask for bet per round
    :param max_bet: int
    :return: int
    """
    while True:
        print('How much do you bet? (1-{}, or (Q)UIT)'.format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'Q':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    """
    Create all 52 cards for play round.
    :return: list
    """
    deck = []
    for suit in CARDS:
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand: list, dealer_hand: list, show_dealer_hand: bool) -> None:
    """
    Show cards without first dialer card.
    :param player_hand: list
    :param dealer_hand: list
    :param show_dealer_hand: bool
    :return: None
    """
    print()
    if show_dealer_hand:
        print('DEALER: ', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])

    print('PLAYER: ', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards: list) -> int:
    """
    Calculate cards values.
    :param cards: list
    :return: int
    """
    value = number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10
    return value


def display_cards(cards: list) -> None:
    """
    Show all cards.
    :param cards: list
    :return: None
    """
    rows = ['', '', '', '']

    # for i, card in enumerate(cards):
    for card in cards:
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def get_move(player_hand: list, money: int) -> str:
    """
    Player moves per round.
    :param player_hand: list
    :param money: int
    :return: str
    """
    while True:
        moves = ['(H)it, (S)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        move_prompt = ','.join(moves) + '> '
        move = input(move_prompt).upper()

        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move
