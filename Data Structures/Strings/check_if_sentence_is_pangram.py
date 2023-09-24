# Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
sentence = "leetcode"
sentence = "thequickbrownfoxjumpsoverthelazydog"

sentence_dict = {}
for i in sentence:
    if i in sentence_dict:
        sentence_dict[i] += 1
    else:
        sentence_dict[i] = 1

if len(sentence_dict) == 26:
    print("True")
else:
    print("False")

# allegedly lesser runtime
# s=set(sentence)
# for i in range(26):
#     if chr(97+i) not in s:
#         return False
# return True
