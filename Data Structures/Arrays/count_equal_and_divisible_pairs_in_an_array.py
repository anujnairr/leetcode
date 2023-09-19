# Count Equal and Divisible Pairs in an Array
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n,
# such that nums[i] == nums[j] and (i * j) is divisible by k.
from collections import defaultdict
nums, k = [1, 2, 3, 4], 1
nums, k = [3, 1, 2, 2, 2, 1, 3], 2
nums, k = [5, 5, 9, 2, 5, 5, 9, 2, 2, 5, 5, 6, 2, 2, 5, 2, 5, 4, 3], 7

seen = defaultdict(int)
pairs = []
count = 0
for i in range(len(nums)):
    if nums[i] not in seen:
        seen[nums[i]] = []
        seen[nums[i]].append(i)
    else:
        for j in seen[nums[i]]:
            pairs.append((i, j))
        seen[nums[i]].append(i)
for (i, j) in pairs:
    if (i*j) % k == 0:
        count += 1
print(count)

# Bruteforce method
# count = 0
# for i in range(0, len(nums)-1):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             if (i*j) % k == 0:
#                 count += 1
# print(count)
