# Find the duplicate number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

nums = [1, 3, 4, 2, 2]

slow = nums[0]
fast = nums[0]

# Now, we will increment slow by one and fast by two steps
# DO Note that in case of a linked list, we do slow.next and slow.next.next as we use the next pointer ofa node
# But here, since all we have at each position is a number, we will increment by using that number as the next pointer/index
while (True):
    slow = nums[slow]
    fast = nums[nums[fast]]
    if (slow == fast):
        break

# Now, once we detect the cycle, now its time to find the starting point of it.
# Just like in a linked list, we will reset our slow pointer to again point to first element
slow = nums[0]

# And now, we increment both pointers one step at a time until they point to the same element.
# The element they will eventually point to is the repeated element
while (slow != fast):
    slow = nums[slow]
    fast = nums[fast]

print(slow)

# Refer: https://leetcode.com/problems/find-the-duplicate-number/solutions/2548490/you-learn-something-new-every-day/

# # sliding window algorithm
# nums.sort()
# print(nums)
# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1]:
#         print(nums[i])


# greater runtime
# m = {}
# for i in nums:
#     if i not in m:
#         m[i] = 1
#     else:
#         m[i] += 1

# for key, value in m.items():
#     if value > 1:
#         print(key)
