# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict, Counter
s = "anagram"
t = "nagaram"
# s, t = "rat", "car"
# s, t = "aa", "a"

ans1 = defaultdict(int)
ans2 = defaultdict(int)

for i in range(len(s)):
    ans1[s[i]] = 1 + ans1.get(s[i], 0)
    ans2[t[i]] = 1 + ans2.get(t[i], 0)

print(ans1, ans2)

if ans1 == ans2:
    print(True)
else:
    print(False)

# another solution
# for i in s:
#     if i in ans1:
#         ans1[i] += 1
#     else:
#         ans1[i] = 1

# for i in t:
#     if i in ans2:
#         ans2[i] += 1
#     else:
#         ans2[i] = 1

# if ans1 == ans2:
#     print(True)


# ans1 = dict(Counter(s))
# ans2 = dict(Counter(t))
# if ans1 == ans2:
#     return True
