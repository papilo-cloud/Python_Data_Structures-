def insertion_sort(list):
    for i in range(1, len(list)):
        temp_value = list[i]
        position = i - 1
        
        while position >= 0:
            if list[position] > temp_value:
                list[position + 1] = list[position]
                position = position - 1
            else:
                break
        list[position + 1] = temp_value
    return list

print(insertion_sort([10, 100, 45, 55, 85, 15, 35]))