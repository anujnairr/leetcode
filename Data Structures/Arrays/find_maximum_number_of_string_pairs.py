# Find Maximum Number of String Pairs

# You are given a 0-indexed array words consisting of distinct strings.
# The string words[i] can be paired with the string words[j] if:
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
# Note that each string can belong in at most one pair.

# words = ["cd", "ac", "dc", "ca", "zz"]
words = ["wk", "xf", "ot", "je", "hd", "kw", "fx", "to", "ej"]
count = 0
temp_array = []
for i in range(len(words)):
    if words[i][::-1] in temp_array:
        count += 1
    temp_array.append(words[i])

print(count)

# double forloop code:
# for i in range(len(words)-1):
#     for j in range(i+1, len(words)):
#         if words[i] == words[j][::-1]:
#             count += 1
# print(count)
