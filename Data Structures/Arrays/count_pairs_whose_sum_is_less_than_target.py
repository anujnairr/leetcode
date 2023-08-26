# Count Pairs Whose Sum is Less than Target
# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

nums = [-1, 1, 2, 3, 1]
target = 2
# nums, target = [-6, 2, 5, -2, -7, -1, 3], -2
count = 0

nums.sort()  # sort the vector nums
c = 0  # variable to store the count
left = 0  # variable to store the left
right = len(nums)-1  # variable to store the right
while (left < right):  # loop until left is less than right
    if (nums[left] + nums[right] < target):  # if nums[left] + nums[right] is less than target
        c = c + right-left  # update the count
        left += 1  # increment the left
    else:  # else
        right -= 1  # decrement the right
print(c)  # return the count

# for i in range(len(nums) - 1):
#     for j in range(i+1, len(nums)):
#         if i < j and nums[i] + nums[j] < target:
#             count = count + 1

# print(count)
