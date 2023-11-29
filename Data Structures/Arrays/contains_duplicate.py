# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1, 2, 3, 1]
hashset = set()

for i in nums:
    if i in hashset:
        print(True)
    hashset.add(i)

# Another solution
# if len(nums) > len(set(nums)):
#     return True
# else:
#     return False
