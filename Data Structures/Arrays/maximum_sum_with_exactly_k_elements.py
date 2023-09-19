# Maximum Sum With Exactly K Elements
# You are given a 0-indexed integer array nums and an integer k.
# Your task is to perform the following operation exactly k times in order to maximize your score:
# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

nums = [1, 2, 3, 4, 5]
k = 3

m_index = nums.index(max(nums))
ans = []
for i in range(0, k):
    m = max(nums)
    ans.append(m)
    m = m+1
    nums[m_index] = m

print(sum(ans))

# maxNum = max(nums)
# sumMax = 0
# for i in range(k):
#     sumMax += maxNum

# more = 0
# for j in range(k):
#     sumMax += more
#     more += 1

# print(sumMax)
