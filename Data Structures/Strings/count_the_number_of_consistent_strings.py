# You are given a string allowed consisting of distinct characters and
# an array of strings words. A string is consistent if all characters in the string appear in
# the string allowed.
# Return the number of consistent strings in the array words.

# allowed = "abc"
# words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
allowed = "cad"
words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
count = 0
for i in words:
    if set(i) - set(allowed):
        pass
    else:
        count += 1
print(count)

# We know that sets in python are actually implemented by hash tables, which means you can search a member in set by O(1).
# Therfore, first we create a set from allowed string and check that every letter of each word to be in the allowed string.
# If its not, we increase the count. By the end of the program we know the number of wrong words,
# so we just need to return the difference of allowed length and count
# Complexity: O(nd)
# If we assume we have n words, we should iterate on all of them and also iterate on each letter which we assumed the average length of words is d.
# So the time complexity is O(nd).
# Code:
# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         allowed = set(allowed)
#         count = 0

#         for word in words:
#             for letter in word:
#                 if letter not in allowed:
#                     count += 1
#                     break

#         return len(words) - count
