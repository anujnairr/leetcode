# Write a function in python that can reverse a string using stack data structure. Use Stack class.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque
string = "We will conquere COVID-19"


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


def reverse_string(string):
    new_stack = Stack()

    for i in string:
        new_stack.push(i)

    rstr = ""
    while new_stack.size() != 0:
        rstr += new_stack.pop()

    return rstr

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.peek())
# s.pop()
# print(s.size())
# print(s.container)


if __name__ == '__main__':
    print(reverse_string(string))
