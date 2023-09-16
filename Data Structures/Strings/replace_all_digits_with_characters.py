# Replace All Digits with Characters
# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

s = "a1c1e1"
ans = ""

# ord converts ascii to value and chr does the vice-versa.


def shift(string, number):
    print(string, number)
    a = chr((ord(string) + number))
    return a


for i in range(len(s)):
    if s[i].isdigit():
        ans += shift(s[i-1], int(s[i]))
    else:
        ans += s[i]

print(ans)
