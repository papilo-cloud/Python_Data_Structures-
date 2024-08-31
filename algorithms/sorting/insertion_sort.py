def insertion_sort(list):
    # The Insertion Sort algorithm uses one part of the array to hold
    # the sorted values, and the other part of the array to hold values
    # that are not sorted yet.
    
    for i in range(1, len(list)):
        temp_value = list[i]
        position = i
        
        while position > 0:
            if list[position - 1] > temp_value:
                list[position] = list[position - 1]
                position -= 1
            else:
                break
        list[position] = temp_value
    return list

print(insertion_sort([10, 100, 45, 55, 85, 15, 35]))