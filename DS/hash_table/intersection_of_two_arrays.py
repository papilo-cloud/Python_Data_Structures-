num1 = ["a", "b", "c", "d", "e",'g','h','i','j','k','l','m','n','o', "f"]
num2 = ['a','o',"f"]
def intersection_of_two_arrays(array1, array2):
    intersection = []
    hash_table = {}
    
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1
    for index in larger_array:
        hash_table[index] = 1
    
    for index in smaller_array:
        if (hash_table.get(index)):
            intersection.append(index)
    return intersection

print(intersection_of_two_arrays(num1, num2))
