# Check if All Characters Have Equal Number of Occurrences
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
s = "abacbc"
# s = "aaabb"

m = {}
for i in s:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1

a = m.values()

# commented lines aren't necessary to assign values to array "a"
# a = []
# for value in m.values():
#     a.append(value)

if len(set(a)) == 1:
    print("True")
