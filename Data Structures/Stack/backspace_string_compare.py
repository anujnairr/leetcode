# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
s = "ab#c"
t = "ad#c"


class Solution(object):
    def backspaceCompare(self, s, t):
        def helper(s):
            s = s
            string = ""
            stack = []
            for i in s:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return helper(s) == helper(t)

# Brute force method:
    stack1, stack2 = [], []

    for i in s:
        if i == '#' and stack1:
            stack1.pop()
        elif i != '#':
            stack1.append(i)

    for j in t:
        if j == '#' and stack2:
            stack2.pop()
        elif j != '#':
            stack2.append(j)

    if stack1 == stack2:
        print(True)
