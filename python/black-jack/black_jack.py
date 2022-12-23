"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    face_cards = ['J','Q','K']
    ace_card = 'A'
    # if card in face_cards:
    #     return 10
    # elif card == ace_card:
    #     return 1
    # else:
    #     return int(card)
    return (
        10 if card in face_cards
        else 1 if card == ace_card
        else int(card)
    )

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_two) > value_of_card(card_one):
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    ace_card = 'A'
    value_of_ace_card = 0
    if ace_card in (card_one,card_two):
        value_of_ace_card = 1
    elif 21 - (card_one_value + card_two_value) >= 11:
        value_of_ace_card = 11
    else:
        value_of_ace_card = 1
    return int(value_of_ace_card)

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    ten_cards = ['J','Q','K','10']
    ace_card = 'A'
    # if card_one in ten_cards and card_two == ace_card:
    #     return True
    # elif card_two in ten_cards and card_one == ace_card:
    #     return True
    # else:
    #     return False
    return card_one in ten_cards and card_two == ace_card or card_two in ten_cards and card_one == ace_card

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    qk = ['Q','K']
    # if card_one_value and card_two_value in qk:
    #     return True
    # elif card_one_value == card_two_value:
    #     return True
    # else:
    #     return False
    return card_one_value and card_two_value in qk or card_one_value == card_two_value

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    total = [9,10,11]
    # if card_one_value + card_two_value in total:
    #     return True
    # else:
    #     return False
    return card_one_value + card_two_value in total
