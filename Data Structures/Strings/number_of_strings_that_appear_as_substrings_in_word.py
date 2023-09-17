# Number of Strings That Appear as Substrings in Word
# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.
patterns = ["a", "abc", "bc", "d"]
word = "abc"
patterns = ["a", "b", "c"]
word = "aaaaabbbbb"
for i in patterns:
    if i in word:
        print("Yes")
