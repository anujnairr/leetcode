# Maximum Product of Two Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
nums = [3, 4, 5, 2]
high, highest = 0, 0
for i in nums:
    if i >= highest:
        high = highest
        highest = i
    elif i >= high:
        high = i

print((highest-1) * (high-1))

# more runtime and easier code.
# nums.sort(reverse=True)
# print(nums)
# print((nums[0]-1) * (nums[1]-1))
