"""Binary search exercise."""


def find(search_list, value):
    """Look for the value given in the list provided."""
    # Set the left and right boundaries
    left = 0
    right = len(search_list) - 1
    # The loop continues as long as the boundaries have not met
    while left <= right:
        # Findig the median usig floor division
        middle_index = (left + right) // 2
        middle_value = search_list[middle_index]
        # The three checks
        if middle_value == value:
            return middle_index
        elif middle_value < value:
            left = middle_index + 1
        else:
            right = middle_index - 1
    raise ValueError("value not in array")
