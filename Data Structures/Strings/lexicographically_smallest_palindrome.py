# Lexicographically Smallest Palindrome
# You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it.
# In one operation, you can replace a character in s with another lowercase English letter.
# Your task is to make s a palindrome with the minimum number of operations possible.
# If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.
# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ,
# string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
# Return the resulting palindrome string.

s = "egcfe"
s = "abcd"
# s = "atie"

s_list = list(s)
l = 0
r = len(s) - 1

while l <= r:
    if s_list[r] > s_list[l]:
        s_list[r] = s_list[l]
    else:
        s_list[l] = s_list[r]
    l += 1
    r -= 1

print("".join(s_list))
