# Given a string s, return the longest palindromic substring in s.
s = "babad"

reslength = 0
res = ""


for i in range(len(s)):
    if len(s) % 2 != 0:
        l = i
        r = i
    else:
        l = i
        r = i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r - l + 1) > reslength:
            reslength = r - l + 1
            res = s[l:r+1]
        l -= 1
        r += 1

print(res)
