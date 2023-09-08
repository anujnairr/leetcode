# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

from collections import Counter

nums = [4, 3, 2, 7, 8, 2, 3, 1]

# BETTER SOLUTION:
m = {}
answer = []
for i in nums:
    if i in m:
        answer.append(i)
    else:
        m[i] = 1

print(answer)

# ALRIGHT SOLUTION:
# a = dict(Counter(nums))

# key_list = []
# for key, value in a.items():
#     if value >= 2:
#         key_list.append(key)

# print(key_list)
