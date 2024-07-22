
def triangular_number(num):
    if num == 1:
        return 1
    else:
        return num + triangular_number(num - 1)

print(triangular_number(7))