# Given an integer array nums and an integer k, 
# return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

nums = [3,2,1,5,4]
k = 2
count = 0
nums.sort()

#o(n^2)
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if abs(nums[i]-nums[j]) == k:
            count+=1

