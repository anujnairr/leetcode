# #  Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# d = {}
# for word in strs:
#     char = "".join(sorted(word))
#     if char not in d:
#         d[char] = [word]
#     else:
#         d[char].extend([word])

# print(d)
# print(d.values())

# Neetcode's solution:
ans = defaultdict(list)

for i in strs:
    count = [0] * 26
    for c in i:
        count[ord(c) - ord("a")] += 1
    ans[tuple(count)].append(i)
print(ans)
print(ans.values())
