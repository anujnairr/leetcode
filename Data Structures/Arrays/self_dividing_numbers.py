# Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
left = 1
right = 22
l = []
for i in range(left, right+1):
    fl, a = 0, i
    if '0' in str(i):
        fl = 1
    else:
        while a != 0:
            if i % (a % 10) != 0:
                fl = 1
                break
            a = a//10
    if fl == 0:
        l.append(i)
print(l)
