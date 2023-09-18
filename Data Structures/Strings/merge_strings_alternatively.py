# Merge Strings Alternately
# # You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# # Return the merged string.
word1 = "abc"
word2 = "pqr"
word1, word2 = "abcd", "pq"
word1, word2 = "ab", "pqrs"

# # more run time
# ans = ""
# # for i in range(min(len(word1), len(word2))):
# #     ans += word1[i] + word2[i]
# # if i < len(word1)-1:
# #     ans += word1[i+1:len(word1)]
# # else:
# #     ans += word2[i+1:len(word2)]
# # print(ans)

result = []
i = 0
while i < len(word1) or i < len(word2):
    if i < len(word1):
        result.append(word1[i])
    if i < len(word2):
        result.append(word2[i])
    i += 1
print(''.join(result))

# OR
# return ''.join(w1 + w2 for w1, w2 in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
