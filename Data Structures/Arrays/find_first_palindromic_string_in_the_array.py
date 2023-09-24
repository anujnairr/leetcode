# Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.
words = ["abc", "car", "ada", "racecar", "cool"]
count = 0

for i in words:
    while count == 0:
        if i == i[::-1]:
            ans = i
            count = 1
        break

if count == 1:
    print(ans)
else:
    print("")

# for word in words:
#     if(word == word[::-1]):
#         return word
# return ""
