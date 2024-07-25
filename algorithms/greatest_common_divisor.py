def gcd(num1, num2):
    if num1 > num2:
        x = num1
        y = num2
    else:
        x = num2
        y = num1
    while x%y != 0:
        remainder = x%y
        x = y
        y = remainder
    return y

print(gcd(44, 12))
    