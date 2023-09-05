# Given two string arrays word1 and word2, 
# return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

word1 = ["ab", "c"]
word2 = ["abcddefg"]
word11 = ""
word22 = ""

for i,j in enumerate(word1):
    word11 += j
for i,j in enumerate(word2):
    word22 += j

if word11 == word22:
    print(True)