# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


nums, k = [1, 1, 1, 2, 2, 3], 2
# nums, k = [1, 2], 2
# nums, k = [3, 0, 1, 0], 1

ans = [[] for x in range(len((nums))+1)]

m = {}
for i in nums:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1

for key, value in m.items():
    ans[value].append(key)

arr = []
result = []
for j in range(len(ans)-1, 0, -1):
    if len(ans[j]) != 0 and len(result) < k:
        result += ans[j]
    #     for l in ans[j]:
    #         arr.append(l)

    # if len(arr) == k:
    #     print(arr)

print(result)
