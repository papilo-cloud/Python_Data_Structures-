def word_builder(list):
    new_list = []
    
    for i in list:
        for j in list:
            if i != j:
                new_list.append(i+j)
                
    return new_list

print(word_builder(['a', 'b', 'c', 'd']))
    