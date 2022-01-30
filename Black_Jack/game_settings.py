
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

MONEY = 1000
CARDS = [HEARTS, DIAMONDS, SPADES, CLUBS]

RULES = """
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    Buttons:
    (H)it to take another card.
    (S)tand to stop taking cards.
    (D)ouble down to increase your bet.
    """

LOOSE = """
    You're broke! \n
    Good thing you weren't playing with real money.\n
    Thanks for playing!
    """