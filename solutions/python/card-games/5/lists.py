"""Track poker hands and assorted card tasks."""


jack = 11


def get_rounds(number: int) -> list:
    """Create a list containing the current and next two round numbers."""
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1, rounds_2: list) -> list:
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int] , number: int) -> bool:
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand: list) -> float:
    """Calculate and return the average card value from the list."""
    return (sum(hand) / len(hand))


def approx_average_is_average(hand: list) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    calculated_average = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2 
    middle_card = hand[len(hand) // 2]
    return calculated_average in (first_last_avg, middle_card)


def average_even_is_average_odd(hand: list) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    even_cards = []
    odd_cards = []
    for index , card in enumerate(hand):
        if index % 2 == 0:
            even_cards.append(card)
        else:
            odd_cards.append(card)
    average_even = sum(even_cards) / len(even_cards) if even_cards else 0
    average_odd = sum(odd_cards) / len(odd_cards) if odd_cards else 0 
    return average_even == average_odd


def maybe_double_last(hand: list) -> list:
    """Multiply a Jack card value in the last index position by 2."""
    if hand and hand[-1] == jack:
        hand[-1] = jack * 2 
    return hand
        
