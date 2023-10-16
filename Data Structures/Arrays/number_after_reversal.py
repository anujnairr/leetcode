# A Number After a Double Reversal
# Reversing an integer means to reverse all its digits.

# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.
num = 0
num = 1800
# num = 526

a = str(num)
b = a[::-1]
b = int(b)

b = str(b)
c = int(b[::-1])

if c == num:
    print(True)

# lesser runtime:
# Observe that the only chance to make double-reversed different from the original is that the original has one or more trailing zeros.
# The reversed will never have any trailing zeros. The easy way to check existence of trailing zeros is modulo 10.
# num = 0 is the edge condition so do check that.
# return num % 10 == 0 or num == 0
