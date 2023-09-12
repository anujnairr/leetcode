# Substrings of Size Three with Distinct Characters

# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

s = "xyzzaz"

s_list = list(s)
print(s_list)
count = 0
for i in range(len(s_list)-2):
    s = "".join(s_list[i:i+3])
    if len(set(s)) == 3:
        count += 1

print(count)
