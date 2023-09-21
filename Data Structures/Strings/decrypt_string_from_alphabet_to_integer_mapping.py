# Decrypt String from Alphabet to Integer Mapping
# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.

s = "10#11#12"
result = []
i = 0
while i < len(s):
    if i+2 < len(s) and s[i+2] == '#':
        decrypt = chr(96 + int(s[i:i+2]))
        result.append(decrypt)
        i += 3
    else:
        decrypt = chr(96 + int(s[i]))
        result.append(decrypt)
        i += 1
print(''.join(result))

# for i in range(3):
#     if s[i] == '#':
#         index = s.index(s[i])
#         print(index)
#         decrypt = chr(96 + int(result[:index]))
#         result = decrypt
#     else:
#         result += s[i]
# print(result)

#     result = result
# s_list = list(s)
# print(s_list)
# ans = ""
# temp = ""
# ans_list = []
# for i in range(len(s_list)):
#     if s[i].isdigit():
#         temp += s[i]
#     if s[i] == '#':
#         decrypt = chr(96 + int(temp))
#         ans_list.append(decrypt)
#         temp = ""

# print(ans_list)
