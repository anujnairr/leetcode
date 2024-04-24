# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if target < nums[m]:
            r = m-1
        elif target > nums[m]:
            l = m+1
        else:
            return m
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

if __name__ == '__main__':
    print(binarySearch(nums, target))
