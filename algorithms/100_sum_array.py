def one_hundred_sum(list):
    left_index = 0
    right_index = len(list) - 1
    
    while left_index < (len(list) / 2):
        if list[left_index] + list[right_index] != 100:
            return False
        left_index += 1
        right_index -= 1
    
    return True

print(one_hundred_sum([90,20,45,30,70,55,80,10]))    
    