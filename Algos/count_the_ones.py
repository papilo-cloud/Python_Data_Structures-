def count_the_ones(list):
    number_count = 0
    
    for inner_list in list:
        for number in inner_list:
            if number == 1:
                number_count += 1
                
    return number_count


lists = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0]
]
print(count_the_ones(lists))

# This function's time complexity is O(N)