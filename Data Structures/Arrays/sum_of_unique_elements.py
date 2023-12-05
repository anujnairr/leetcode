# Sum of unique elements
# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

from collections import defaultdict
nums = [1, 2, 3, 2]

# m = {}
# for i in range(len(nums)):
#     if nums[i] in m:
#         m[nums[i]] += 1
#     else:
#         m[nums[i]] = 1
# print(m)
# ans = 0
# for i, j in m.items():
#     if j == 1:
#         ans = ans + i
# print(ans)

# better runtime:
ans = [0] * 101
for i in nums:
    ans[i] += 1
print(ans)

result = 0
for i in nums:
    if ans[i] == 1:
        result += i
print(result)
