# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.

# A word is a maximal  substring consisting of non-space characters only.

# s = "luffy is still joyboy"
s = "   fly me   to   the moon  "
d = s.split()
# d = s.strip(" ")
print(d)
# d = d.split()
print(len(d[-1]))
# using for loop but it isn't needed.
# d.reverse()
# count = 0
# for i in d[0]:
#   count+=1
# print(count)