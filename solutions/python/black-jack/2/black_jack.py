"""Functions to help play and score a game of blackjack."""
def value_of_card(card):
    if card in('J' , 'Q' , 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return card_one , card_two


def value_of_ace(card_one , card_two):
    """Calculate the most advantageous value for the ace card."""
    if card_one == 'A' or card_two == 'A':
        return 1
    total_points = value_of_card(card_one) + value_of_card(card_two)
    if total_points + 11 <= 21:
        return 11
    return 1 


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    tens = ('10' , 'K' , 'Q' , 'J')
    return (card_one == 'A' and card_two in tens) or (card_two == 'A' and card_one in tens)


def can_split_pairs(card_one , card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one , card_two):
    """Determine if a blackjack player can place a double down bet."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9 , 10 , 11)
    
