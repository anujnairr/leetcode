# Unique Morse Code Words
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.

# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
# We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

morsecode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
letters = "abcdefghijklmnopqrstuvwxyz"
words = ["gin", "zen", "gig", "msg"]
m = dict(zip(letters, morsecode))
print(m)
ans = []

for word in words:
    string = ""
    for i in word:
        string += m[i]
    ans.append(string)

print(set(ans))

# #different code
# s = set()
# mos = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
#        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

# for w in words:
#     m = ''
#     for l in w:
#         m += mos[ord(l) - ord('a')]
#     s.add(m)

# print(len(s))
