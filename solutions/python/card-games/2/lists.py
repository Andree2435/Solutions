"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    first_round = [number, number + 1, number + 2]
    return first_round

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)
    


def approx_average_is_average(hand):
    """Check if a simplified average matches the actual average."""
    true_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return true_average in (first_last_average, middle_card)


def average_even_is_average_odd(hand):
    """Return if the average of even-indexed card values equals that of odd-indexed card values."""
    even_cards = hand[0::2]
    odd_cards = hand[1::2]

    avg_even = sum(even_cards) / len(even_cards)
    avg_odd = sum(odd_cards) / len(odd_cards)

    return avg_even == avg_odd



def maybe_double_last(hand):
    """Multiply the last card by 2 if it's a Jack (value 11)."""
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand