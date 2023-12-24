# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
from collections import deque
s = "()[]{}"

dictionary = {
    ')': '(',
    '}': '{',
    ']': '['
}


def valid_parentheses(s):
    stack = []
    for i in s:
        if i in dictionary:
            if stack and stack[-1] == dictionary[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False


print(valid_parentheses(s))

# codebasics solution
# class Stack:
#     def __init__(self):
#         self.container = deque()

#     def push(self, val):
#         self.container.append(val)

#     def pop(self):
#         return self.container.pop()

#     def peek(self):
#         return self.container[-1]

#     def is_empty(self):
#         return len(self.container) == 0

#     def size(self):
#         return len(self.container)

# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2


# def is_balanced(s):
#     stack = Stack()
#     for ch in s:
#         if ch=='(' or ch=='{' or ch == '[':
#             stack.push(ch)
#         if ch==')' or ch=='}' or ch == ']':
#             if stack.size()==0:
#                 return False
#             if not is_match(ch,stack.pop()):
#                 return False

#     return stack.size()==0


# if __name__ == '__main__':
#     print(is_balanced("({a+b})"))
#     print(is_balanced("))((a+b}{"))
#     print(is_balanced("((a+b))"))
#     print(is_balanced("((a+g))"))
#     print(is_balanced("))"))
#     print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
