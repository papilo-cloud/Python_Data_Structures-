# time complexity O(N^2)
def greatest_number1(array):
    for i in range(len(array)):
        max_num = True
        for j in range(len(array)):
            if array[j] > array[i]:
                max_num = False
        if max_num:
            return array[i]
            
# print(greatest_number([52,7,23,14,35]))

# time complexity O(N)
def greatest_number2(array):
    max_num = array[0]
    
    for elem in array:
        if elem > max_num:
            max_num = elem
    return max_num

print(greatest_number2([52,77,23,14,35]))