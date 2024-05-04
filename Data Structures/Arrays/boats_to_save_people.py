# You are given an array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.
people = [1, 2]
limit = 3

boat = 0
l = 0
r = len(people)-1
people.sort()

while l <= r:
    remain = limit - people[r]
    boat += 1
    r -= 1
    if l <= r and remain >= people[l]:
        l += 1

print(boat)
