# Relative Ranks
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on.
# The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

from collections import defaultdict

score = [10, 3, 8, 9, 4]

hashmap = defaultdict(int)

for i in range(len(score)):
    hashmap[score[i]] = i

print(hashmap)

score_copy = score.copy()

score_copy.sort(reverse=True)

print(score_copy)

rank = [""] * len(score_copy)

for i in range(len(rank)):
    if i == 0:
        # score_copy[i] will be the first position 10, in hashmap, first position 10 value is index 0 and hence rank[0] is assigned "Gold Medal"
        rank[hashmap[score_copy[i]]] = "Gold Medal"
    elif i == 1:
        rank[hashmap[score_copy[i]]] = "Silver Medal"
    elif i == 2:
        rank[hashmap[score_copy[i]]] = "Bronze Medal"
    else:
        rank[hashmap[score_copy[i]]] = str(i+1)

print(rank)
