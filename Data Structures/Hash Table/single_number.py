# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

nums = [2, 2, 1]
nums = [4, 1, 2, 1, 2]

m = {}
for i in nums:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1

for key, value in m.items():
    if value == 1:
        print(key)
