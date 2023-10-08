# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
nums = [3, 0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

for i in range(len(nums)+1):
    if i not in nums:
        print(i)

# less run time
# n = len(nums)
# return ((n * (n+1)) // 2 ) - sum(nums)

# Initialize a variable n as the length of the array nums plus 1, assuming that the missing number is the last number in the sequence.
# Calculate the expected sum of the sequence from 0 to n (inclusive) using the formula (n * (n - 1)) / 2.
# Iterate over each number in nums and subtract it from the total variable, which represents the expected sum.
# After the loop, the total will contain the missing number.
# Return the value of total.
