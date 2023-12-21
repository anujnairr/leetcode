from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        self.container.pop()

    def peek(self):
        print(self.container[-1])

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        print(len(self.container))


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print(s, s.container)
s.peek()
print(s.is_empty())
s.size()
