
num1 = ["a", "b", "c", "d", "e",'g','h','i','j','k','l','m','n','o', "f"]
num2 = ['o',"f"]

# Using an array
# time complexity is O(N*M)
def array_subsets(array1, array2):
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1
        
    for i in smaller_array:
        found_match = False
        for j in larger_array:
            steps += 1
            if i == j:
                found_match = True
                break
            
        if found_match == False:
            return False
    return True

# Using a hashtable/dictionary
# time complexity is O(1)
def array_subsets1(array1, array2):
    hash_table = {}
    steps = 0
    
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1
        
    for index in larger_array:
        hash_table[index] = True
        
    for value in smaller_array:
        steps += 1
        if (hash_table.get(value) == None):
            print(steps)
            return False
        
    print(steps)
    return True
        
print(array_subsets1(num1, num2))