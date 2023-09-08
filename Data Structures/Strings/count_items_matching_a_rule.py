# You are given an array items, where each items[i] = [typei, colori, namei] 
# describes the type, color, and name of the ith item. 
# You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

count = 0
rules = ["type", "color", "name"]

index = rules.index(ruleKey)
print(index)

for i in range(len(items)):
    if ruleValue == items[i][index]:
        count+=1
print(count)

# Different solution:
# tot = 0
# if ruleKey == "type":
#     rk = 0
# elif ruleKey == "color":
#     rk = 1
# elif ruleKey == "name":
#     rk = 2
# types = [item[rk] for item in items]
# for idx, item in enumerate(types):
#     if item == ruleValue:
#         tot += 1
# print(tot)