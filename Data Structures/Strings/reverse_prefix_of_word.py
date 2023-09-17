# Reverse Prefix of Word
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# word, ch = "abcdefd", "d"
# word, ch = "xyxzxe", "z"
word, ch = "abcd", "z"

global ans


def manipulation(word, ch):
    ch_index = word.index(ch)
    ans = "".join(word[ch_index::-1] + word[ch_index+1:])
    return ans


if ch in word:
    print(manipulation(word, ch))
else:
    print(word)

# lesser runtime:
# index = word.find(ch)

# if index == -1:
#     return word
# else:
#     return word[index::-1] + word[index + 1:]
