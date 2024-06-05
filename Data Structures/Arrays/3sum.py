# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

nums = [-1, 0, 1, 2, -1, -4]
res = []
nums.sort()

for i, a in enumerate(nums):
    if i > 0 and a == nums[i-1]:
        continue

    l = i+1
    r = len(nums) - 1
    while l < r:
        threesome = a + nums[l] + nums[r]
        if threesome > 0:
            r -= 1
        elif threesome < 0:
            l += 1
        else:
            res.append([a, nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]:
                l += 1

print(res)
