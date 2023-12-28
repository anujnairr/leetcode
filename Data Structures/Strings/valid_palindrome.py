# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

s = "A man, a plan, a canal: Panama"
s = "race a car"
# s = "0P"

z = []
for i in s:
    if i.isalnum():
        z.append(i.lower())

left = 0
right = len(z) - 1

while left <= right:
    print(left, right)
    if z[left] != z[right]:
        print(False)
    left += 1
    right -= 1

print(True)

# To check if the character is alphanumeric without using isalnum() function:
# ord('A') < ord(i) < ord('Z') or ord('1') < ord(i) < ord('9') or ord('a') < ord(i) < ord('z')
