
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

n = 2
arr = [] * n
arr.append(0)
for i in range(1, n+1):
    sum = 0
    while i != 0:
        temp = i % 2
        if temp == 1:
            sum += 1
        i = i//2
    arr.append(sum)

print(arr)

# Neetcode's solution

dp = [0] * (n+1)
offset = 1
for i in range(1, n+1):
    if 2 * offset == i:
        offset = i
    dp[i] = 1 + dp[i - offset]

print(dp)
