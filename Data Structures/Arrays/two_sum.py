nums = [2, 7, 11, 15]
target = 9
# nums = [2, 1, 5, 3]
# target = 4

# How this hash-map solution works: we iterate over each element and create a dictionary m{} of value:index.
# Since the solution is guaranteed, we check if the target - i element in the array is equal to an value which is already part of the hashmap.
# If its not, we continue creating the hashmap until we reach an answer where target - i = an element already in the hashmap.
# We do not have to traverse the array anymore, and return the index of the (target - i) element from the hashmap and the current element.
# O(n) complexity except dictionary keeps increasing with the array size.

m = {}

for i in range(len(nums)):
    temp = target - nums[i]

    if temp not in m:
        m[nums[i]] = i
    else:
        print([m[temp], i])

# Neetcode's solution would be:
# for i, n in enumerate(nums):
#     temp = target - n
#     if temp in m:
#         return [i, m[temp]]
#     m[n] = i
