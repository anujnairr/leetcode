# Given an integer array nums, find the subarray with the largest sum, and return its sum.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curSum = 0
maxSub = nums[0]

for n in nums:
    if curSum < 0:
        curSum = 0
    curSum += n
    maxSub = max(maxSub, curSum)

print(maxSub)
