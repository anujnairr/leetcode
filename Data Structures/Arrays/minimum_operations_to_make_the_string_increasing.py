# Minimum Operations to Make the Array Increasing
# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.

nums = [1, 5, 2, 4, 1]
count = 0
i = 0
ans = 0
# better runtime
# ans = 0
# for i in range(1, len(nums)):

#     if nums[i] <= nums[i - 1]:
#         ans += (nums[i - 1] - nums[i] + 1)
#         nums[i] = (nums[i - 1] + 1)
#         print(ans, nums)
# print(nums,ans)

while i <= len(nums)-2:
    if nums[i] < nums[i+1]:
        pass
    else:
        count = nums[i] - nums[i+1] + 1
        ans += count
        nums[i+1] += count
        print(nums[i+1])
    i += 1
print(nums, ans)
