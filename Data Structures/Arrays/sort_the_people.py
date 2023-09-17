# Sort the People
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
ans_list = []
for a, b in (sorted(zip(heights, names), reverse=True)):
    print(a, b)
    ans_list.append(b)

print(ans_list)

# REFER: https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other
