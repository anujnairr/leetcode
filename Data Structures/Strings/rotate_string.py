# Given two strings s and goal, 
# return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
 
s = "abcde"
goal = "cdeab"
g = list(goal)
d = list(s)
for i in range(len(d)):
    for j in range(len(d)-1):
        t = d[j+1]
        d[j+1] = d[j]
        d[j] = t
    if d == g:
        print("True")

#least runtime.

# class Solution(object):
#     def rotateString(self, s, goal):
#         if len(s) != len(goal):
#             return False
#         double_s = s + s
#         return goal in double_s

# class Solution(object):
#     def rotateString(self, A, B):
#         """
#         :type s: str
#         :type goal: str
#         :rtype: bool
#         """
#         if len(A)==len(B):
#             if B in A+A:
#                 return True
#         else:
#             return False