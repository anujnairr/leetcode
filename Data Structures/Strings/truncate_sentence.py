# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​.
# You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

s = "Hello how are you Contestant"
k = 4

answer_list = (s.split())
print(" ".join(answer_list[0:k]))

# Using for loop
# answer_string = ""
# answer_string = answer_list[0]
# for i in range(1, k):
#     answer_string += " " + answer_list[i]

# print(answer_string)
