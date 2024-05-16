# Given two binary strings a and b, return their sum as a binary string.
a = "1010"
b = "1011"
# a = "11"
# b = "1"

a = a[::-1]
b = b[::-1]

ans = ""
carry = 0

for i in range(max(len(a), len(b))):
    DigitA = int(a[i]) if i < len(a) else 0
    DigitB = int(b[i]) if i < len(b) else 0

    print(DigitA, DigitB)

    total = DigitA + DigitB + carry
    string = str(total % 2)
    ans += string
    carry = total // 2
    print(total, string, ans, carry)

if carry:
    ans = "1" + ans

print(ans)
