string = ['a','o',"f", 'z', 'c', 'd']

def finding_duplicates(array):
    hash_table = {}
    
    for index in array:
        if (hash_table.get(index) == None):
            hash_table[index] = True
        else:
            return index
            
    return hash_table

print(finding_duplicates(string))