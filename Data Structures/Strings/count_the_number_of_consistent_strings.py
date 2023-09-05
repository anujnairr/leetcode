# You are given a string allowed consisting of distinct characters and 
# an array of strings words. A string is consistent if all characters in the string appear in
# the string allowed.

# Return the number of consistent strings in the array words.


allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
count = 0
a = []

for w in words:
    a.append((list(w)))
print(a)