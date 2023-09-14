# Find the Highest Altitude
# There is a biker going on a road trip.
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where
# gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

# The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
gain = [-5, 1, 5, 0, -7]
ans = []
ans.append(0)
highest = 0
for i in range(len(gain)):
    new = ans[i] + gain[i]
    ans.append(new)
    if new > highest:
        highest = new

print(highest)

# Better solutions: it a rolling sum of the array.
# for alt in gain:
#     rollingSum += alt
#     if rollingSum > maxSum:
#         maxSum =  rollingSum
# return maxSum

# for x in gain:
#     curr+=x
#     h=max(curr,h)
# return h
