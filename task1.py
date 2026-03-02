class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def size(self):
        return len(self.data)