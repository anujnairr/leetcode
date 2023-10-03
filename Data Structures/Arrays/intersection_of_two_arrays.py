# Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

nums1 = [4, 9, 9, 5]
nums2 = [9, 4, 9, 8, 4]

temp = set()
tnums1 = set(nums1)
tnums2 = set(nums2)
for i in tnums1:
    if i in tnums2:
        temp.add(i)
print(list(temp))

# less runtime
# ans = []
# for i in set(nums2):
#     if i in nums1:
#         ans.append(i)
# print(ans)
