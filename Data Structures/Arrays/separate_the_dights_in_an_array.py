# Separate the Digits in an Array
#  Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

nums = [135, 25, 83, 77]

ans = []
for i in range(len(nums)):
    nums[i] = str(nums[i])
    print(nums[i])
    ans.extend(nums[i])
    print(ans)

answer = []
for i in ans:
    answer.append(int(i))
print(answer)

# lst1=[]
# for i in nums[::-1]:
#     while i>0:
#         lst1+=[i%10]
#         i=i//10

# return lst1[::-1]
