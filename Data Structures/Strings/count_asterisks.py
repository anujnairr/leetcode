# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
# Note that each '|' will belong to exactly one pair.

s = "l|*e*et|c**o|*de|"
# s = "yo|uar|e**|b|e***au|tifu|l"
count = 0
ans = 0

s = s.split('|')
print(s)
c = 0
for i in range(0, len(s), +2):
    c += s[i].count('*')

print(c)


# more runtime
# for i in range(len(s)):
#     if s[i] == '|':
#         count += 1

#     if count % 2 == 0 and s[i] == '*':
#         ans += 1

# print(ans)
