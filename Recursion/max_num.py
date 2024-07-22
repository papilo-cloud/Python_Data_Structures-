
def max_num(array, index = 0):
    if index == len(array):
        return array[0]
    
    max = max_num(array, index + 1)
    
    if array[index] > max:
        return array[index]
    else:
        return max

print(max_num([11, 4, 6, 3, 22, 9, 7, 10]))
