# Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

nums = [4, 3, 2, 7, 8, 2, 3, 1]

nums_set = set(nums)
print(nums_set)

number_set = set(range(1, len(nums)+1))
print(number_set)

result = number_set - nums_set
print(list(result))


# Different solution:
# answer = []
# i = 1
# while i <= len(nums):
#     if i in nums:
#         pass
#     else:
#         answer.append(i)
#     i += 1
# print(answer)
