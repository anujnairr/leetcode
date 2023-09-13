# Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
s = "Let's take LeetCode contest"

l = s.split()
l1 = []
for i in l:
    l1.append(i[::-1])
r = " ".join(l1)
print(r)

# s = s.split(' ')
# for i, word in enumerate(s):
#     s[i] = word[::-1]
# print(' '.join(s))

# more runtime in the below code:
# split_list = s.split()
# answer_list = []
# string = ""
# for i in range(len(split_list)):
#     answer_list.append(list(split_list[i]))
#     print(answer_list)
#     answer_list[i].reverse()

# print(answer_list)

# for i in answer_list:
#     string += "".join(i) + " "

# print(string.strip())
