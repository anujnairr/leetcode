# Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

ans = []

print([list(set(nums1)-set(nums2)), list(set(nums2)-set(nums1))])

# for i in set(nums1):
#     if i not in nums2:
#         ans[0].append(i)


# for i in set(nums2):
#     if i not in nums1:
#         ans[1].append(i)

# print(ans)
