# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

from collections import Counter
nums = [2, 1, 2, 5, 3, 2]
my_dict = dict((Counter(nums)))
v = 0
k = 0
for key, value in my_dict.items():
    if value > v:
        v = value
        k = key

print(k, v)

# array = []
# for i in range(len(nums)-1):
#     count = 0
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             count += 1
#         array.append(count)

# print(array)
