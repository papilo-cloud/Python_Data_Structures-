def has_duuplicate_value(array):
    array.sort()
    
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    return False

print(has_duuplicate_value([5,9,3,2,4,5,6]))