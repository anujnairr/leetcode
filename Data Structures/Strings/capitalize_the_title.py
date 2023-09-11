# You are given a string title consisting of one or more words separated by a single space,
# where each word consists of English letters.
# Capitalize the string by changing the capitalization of each word such that:

# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

# title = "capiTalIze tHe title"
title = "i lOve leetcode"

answer_list = (title.lower()).split(' ')

for i in range(len(answer_list)):
    if len(answer_list[i]) > 2:
        answer_list[i] = answer_list[i].title()

print(" ".join(answer_list))
