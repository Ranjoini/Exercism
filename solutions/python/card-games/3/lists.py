"""Functions for tracking poker hands and assorted card tasks."""
def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return list(range(number, number + 3))
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds
def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return (sum(hand) / len(hand))
def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    calculated_average = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2 
    middle_card = hand[len(hand) // 2]
    return calculated_average in (first_last_avg, middle_card)
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    even_cards = hand[0::2]
    odd_cards = hand[1::2]
    average_even = sum(even_cards) / len(even_cards)
    average_odd = sum(odd_cards) / len(odd_cards)
    return average_even == average_odd
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    jack = 11
    if hand and hand[-1] == jack:
        hand[-1] = jack * 2 
    return hand
        
