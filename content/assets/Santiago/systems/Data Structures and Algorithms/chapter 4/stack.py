class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Raises if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"Stack({self.items})"


# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)          # Stack([1, 2, 3])
    print(s.peek())   # 3
    print(s.pop())    # 3
    print(s)          # Stack([1, 2])
    print(len(s))     # 2