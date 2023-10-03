# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
nums, k = [1, 1, 1, 2, 2, 3], 2
nums, k = [1, 2], 2
# nums, k = [3, 0, 1, 0], 1

# m = {}
# ans = []
# for i in nums:
#     if i in m:
#         m[i] += 1
#     else:
#         m[i] = 1

# # value_array = []
# # for key, value in m.items():
# #     value_array.append(value)
# # print(value_array)

# print(f"my dictionary is {m}")
# i = 1
# while i <= k:
#     ans.append("Yes")
#     i += 1

# print(f"my answer is {ans}")


count = {}
freq = [[] for i in range(len(nums) + 1)]
print(freq)

for n in nums:
    count[n] = 1 + count.get(n, 0)
for n, c in count.items():
    freq[c].append(n)
    print(freq)

res = []
for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
        print(res)
        if len(res) == k:
            print(res)

        # O(n)
