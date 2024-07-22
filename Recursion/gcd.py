
def gcd(num1, num2):
    if num1 > num2:
        x = num1
        y = num2
    else:
        x = num2
        y = num1
        
    if (x % y != 0):
        remainder = x % y 
        return gcd(y, remainder)
    return y 

print(gcd(10005, 1000))
        