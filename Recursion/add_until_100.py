def add_until_100_1(array, index = 0):
    
    if len(array) == index:
        return 0
    if array[index] + add_until_100_1(array, index + 1) > 100:
        return add_until_100_1(array, index + 1)
    else:
        return array[index] + add_until_100_1(array, index + 1)

print(add_until_100_1([1,2,3,4,5,6,7,8,9,2,10,40]))

# The first function is making unnecessary recursive call
# The problem is that we have two two recursive calls to the function
# within itself. We can easily reduce it to one:

def add_until_100_2(array, index = 0):
    if len(array) == index:
        return 0
    
    sum_of_array = add_until_100_2(array, index + 1)
    
    if array[index] + sum_of_array > 100:
        return sum_of_array
    else:
        return array[index] + sum_of_array

print(add_until_100_2([1,2,3,4,5,6,7,8,9,10]))