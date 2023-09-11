# Detect Capital
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

word = "USA"
word = "FlaG"

if word.isupper():
    print(True)
elif word[1:len(word)].islower():
    print(True)
elif word.islower():
    print(True)
else:
    print(False)

    # another way of writing the above
    # if word.isupper():
    #     return True

    # if word.islower():
    #     return True

    # if word[0].isupper() and word[1:].islower():
    #     return True

    # return False
