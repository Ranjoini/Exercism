"""Variable length quantity."""


def encode(numbers: list[int]) -> list[int]:
    """Encode the number to the variable length format."""
    # create a list to hold the final product
    result = []
    for number in numbers:
        # the chunks list handles all the dirty work of processing
        chunks = []
        # Chop off the first seven bits of data then put them in the chunks list
        chunks.append(number & 127)
        # Push the conveyor belt 7 times to the left to get rid of the numbers we already checked
        number >>= 7
        # If the number is greater than zero, say maybe 00000001, we chop off the number to 7 bits from the right
        while number > 0:
            chunk = number & 127
            # Glue a one in the front to, it will help with the decoding
            chunk = chunk | 128
            # Then use insert(index, element) to add the number to the front of the list to get the desired layout
            chunks.insert(0, chunk)
            number >>= 7
        result.extend(chunks)
    return result


def decode(bytes_list: list[int]) -> list[int]:
    """Decode the number from variable length format back to normal."""
    result = []
    current_number = 0
    is_incomplete = False
    for byte in bytes_list:
        # Strip off the traffic lights we set like the 1..... or 0......
        data = byte & 127
        # Slot it the new data by creating new space, this time shifting the current number to the left instead to make space
        current_number = (current_number << 7) | data
        # Check the traffic lights
        if (byte & 128) == 0:
            # If the trafiic light is off (0) we return the list as complete.
            result.append(current_number)
            current_number = 0
            is_incomplete = False
        else:
            # If not (1) we continue looping
            is_incomplete = True
    # If the sequence ended without a stop signal siganl a value error.
    if is_incomplete:
        raise ValueError("incomplete sequence")
    return result
