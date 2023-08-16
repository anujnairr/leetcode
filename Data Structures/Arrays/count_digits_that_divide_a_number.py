# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.
num = 121
nums = num
count = 0

while num > 0:
    digit = int(num % 10)

    if nums % digit == 0:
        count = count + 1
    num = int(num/10)

print(count)


# num2 = str(num)
# for i in range(len(num2)):
#     if num % int(num2[i]) == 0:
#         count = count + 1
