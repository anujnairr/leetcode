# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

s = "RLRRRLLRLL"
countR = 0
countL = 0
countcombo = 0

for i in s:
    if i == 'R':
        countR += 1
        print(f"countR : {countR}")
    else:
        countL += 1
        print(f"countL : {countL}")
    if countR == countL:
        countcombo += 1
        print(f"countcombo : {countcombo}")

print(countcombo)
