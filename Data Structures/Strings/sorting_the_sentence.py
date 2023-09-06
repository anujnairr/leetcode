# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of lowercase and uppercase English letters.
# A sentence can be shuffled by appending the 1-indexed word position to each word then
# rearranging the words in the sentence.

s = "is2 sentence4 This1 a3"
# s = "Myself2 Me1 I4 and3"
z = {}
a = s.split()

for i in a:
    # generate the numeric value and -1 to find the index of the list
    index = int(i[-1]) - 1
    print(index)
    print(i[-len(i):-1])
    z[index] = i[-len(i):-1]

x = dict(sorted(z.items()))
print(x)

y = ""
for i in x.values():
    y = y + i + " "
print(y)
