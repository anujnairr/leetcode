# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

s = "abccccdd"

d = {}
odd = 0
sum = 0

for i in s:
    d[i] = 1 + d.get(i, 0)

for i in d.values():
    if len(d) == 1:
        print(d[i])
    else:
        if i > 1:
            if i % 2 == 0:
                sum += i
            else:
                sum += i - 1
                odd += 1
        else:
            odd += 1

if odd > 0:
    sum += 1

print(sum)
