# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1.
# It is guaranteed that there will be at most one pivot index for the given input.


# Note The sum of a AP series given first and last term is n / 2 [first term + last term ]
# The value of x is going to sqrt((n2 + n) / 2 )
from math import sqrt
n = 8

temp = (n * n + n) // 2
sq = int(sqrt(temp))
if sq * sq == temp:
    print(sq)
print(-1)
