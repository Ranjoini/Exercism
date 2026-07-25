"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add person name to correct queue given their ticket type."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)        
    return normal_queue


def find_my_friend(queue, friend_name):
    """Finds the name in the given queue and returns their index position."""
    queue_lookup = {name: index for index, name in enumerate(queue)}
    if friend_name in queue_lookup:
        return queue_lookup[friend_name]
    return "Friend not found"


def add_me_with_my_friends(queue, index, person_name):
    """Adds person name at a specified index in a given queue."""
    safe_index = min(max(0, index), len(queue))
    queue.insert(index , person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove person form queue given their name."""
    if person_name in queue:
        queue.remove(person_name)
        return queue

def how_many_namefellows(queue, person_name):
    """Check how many times a given name is repeated."""
    return queue.count(person_name)
    

def remove_the_last_person(queue):
    """Remove the last person from the queue."""
    return queue.pop()


def sorted_names(queue):
    """Sort names in queue in alphabetical order"""
    return sorted(queue)