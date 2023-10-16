# Counting Words With a Given Prefix
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# words = ["pay", "attention", "practice", "attend"]
# pref = "at"
# words = ["leetcode", "win", "loops", "success"]
# pref = "code"
words = ["udt", "ipbjt", "itjbniqf", "iwcsd", "iv", "ezljsxgrv", "ixkxv", "iwcyrwi", "ig", "iwrkov", "izm", "imuusv", "iphigkdxxs", "g", "ildeyvbz", "ibywdj", "ifctnctguw", "ipqnn", "td", "iscvdjx", "ebsy", "cl", "ik", "ik", "ionapx", "ikhbyzyjq", "iuib", "ijobcngoob", "io", "iyvcuronb", "ivopadcf", "iw", "isd", "iiv", "xzxsfcgz", "ikusrhkqc",
         "sywa", "iw", "my", "ivojahjdl", "imxyhpttr", "ivpdleigq", "is", "iyxmbyssga", "igvjeuxnmf", "ircdd", "irz", "iwjlvbrunc", "yefbv", "ipcs", "wxvhccv", "ihythcmyj", "iwgvdonax", "irxozbyu", "vwtees", "ithdg", "izhlb", "kb", "ieejxccn", "byaf", "ixip", "cao", "ipajauzv", "iqxns", "iqpjkrpy", "iu", "puehsn", "iqxcavuat", "ycqewlca", "iaj"]
pref = "i"

sum = 0

# lesser runtime
l = len(pref)
for i in words:
    if i[:l] == pref:
        sum += 1

# one solution:
# for word in words:
#     if word.startswith(pref):
#         sum += 1

print(sum)
