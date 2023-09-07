# Given a list of strings words and a string pattern, 
# return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p 
# so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: 
# every letter maps to another letter, and no two letters map to the same letter.

from collections import defaultdict
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

def find(word):
    l = []
    m = defaultdict(int)
    i = 0
    for c in word:
        if c in m:
            l.append(m[c])
        else:
            i+=1
            m[c] = i
            l.append(m[c])
    
    return l
   
pattern_find = find(pattern)
print(pattern_find)
ans = []
for w in words:
    word_find = find(w)
    if word_find == pattern_find:#check if numeric pattern of pattern is equal to pattern of word 
        ans.append(w)

print(ans)
        
    