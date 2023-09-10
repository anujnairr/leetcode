# Given an array of strings words and a string s, determine if s is an acronym of words.
# The string s is considered an acronym of words if it can be formed by
# concatenating the first character of each string in words in order.
# For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from
# ["bear", "aardvark"].
# Return true if s is an acronym of words, and false otherwise.


words = ["alice", "bob", "charlie"]
s = "abc"
answer = ""
for i in words:
    answer += i[0]
if answer == s:
    print(True)

# lesser line code:
# acronym = ""
# for word in words:
#    acronym += word[0]
# return s == acronym
