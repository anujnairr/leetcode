# Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once.
# Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
nums = [2, 2, 3, 2]
nums = [0, 1, 0, 1, 0, 1, 99]

m = {}

for i in nums:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1

for key, value in m.items():
    if value == 1:
        print(key)
