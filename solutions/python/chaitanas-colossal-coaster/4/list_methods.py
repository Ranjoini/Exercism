"""
Module for managing amusement park ride queues.
Optimized using native list search patterns and defensive error boundaries.
"""

from typing import List, Union


def add_me_to_the_queue(
    express_queue: List[str],
    normal_queue: List[str],
    ticket_type: int,
    person_name: str,
) -> List[str]:
    """Adds a person to the correct queue based on their ticket classification."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: List[str], friend_name: str) -> Union[int, str]:
    """
    Finds the name in the queue and returns their index position.
    Uses native C-level lookups instead of allocating a temporary dictionary.
    """
    try:
        # .index() immediately returns the slot number where the string matches
        return queue.index(friend_name)
    except ValueError:
        # If the name isn't in the list, .index() raises a ValueError
        return "Friend not found"


def add_me_with_my_friends(queue: List[str], index: int, person_name: str) -> List[str]:
    """Inserts a person into a specific position within the queue."""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(
    queue: List[str], person_name: str
) -> Union[List[str], None]:
    """Removes a specific person from the queue if they exist."""
    if person_name in queue:
        queue.remove(person_name)
        return queue
    return None


def how_many_namefellows(queue: List[str], person_name: str) -> int:
    """Counts the total occurrences of an identical name in the queue."""
    return queue.count(person_name)


def remove_the_last_person(queue: List[str]) -> str:
    """Removes and returns the final person standing in the queue."""
    return queue.pop()


def sorted_names(queue: List[str]) -> List[str]:
    """Returns a brand-new list containing the queue names sorted alphabetically."""
    return sorted(queue)
