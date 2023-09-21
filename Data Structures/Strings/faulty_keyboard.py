# Faulty Keyboard
# # Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written.
# Typing other characters works as expected.
# # You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
# # Return the final string that will be present on your laptop screen.
s = "string"
s = "poiinter"

s1 = ''
for i in s:
    if i == 'i':
        s1 = s1[::-1]
    else:
        s1 += i
print(s1)

# # more runtime
# s_list = []
# for i in range(len(s)):
#     if s[i] == 'i':
#         s_list.reverse()
#     else:
#         s_list.append(s[i])

# print(s_list)
