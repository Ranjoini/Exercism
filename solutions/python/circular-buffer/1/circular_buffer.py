class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def read(self):
        """Return the oldest data on the list."""
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")
        return self.buffer.pop(0)

    def write(self, data):
        """Use append() add the data to the end of the list if not full."""
        # Check if the length of the list is at full capacity
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        # If not full let the data in
        self.buffer.append(data)

    def overwrite(self, data):
        """Overwrite an existing peice of data."""
        # Capacity check
        if len(self.buffer) == self.capacity:
            # Kick out the oldest data
            self.buffer.pop(0)
        # Operates like the write method if the ride is not full
        self.buffer.append(data)

    def clear(self):
        """Delete everything."""
        return self.buffer.clear()
