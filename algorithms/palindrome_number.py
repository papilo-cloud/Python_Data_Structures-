def fact(n):
    init = n
    rev = 0
    if n < 0:
        return False
    while n != 0:
        rev = rev * 10 + (n % 10)
        n //= 10
        
    return (rev == init)

    

x = -2147447412
print(fact(x))