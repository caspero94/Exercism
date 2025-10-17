class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            data = self.buffer[0]
            del self.buffer[0]
            return data

    def write(self, data):
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")
        else:
            self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        elif len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            del self.buffer[0]
            self.buffer.append(data)

    def clear(self):
        self.buffer = []

