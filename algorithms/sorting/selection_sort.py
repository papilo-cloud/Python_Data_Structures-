def selection_sort(list):
    # The Selection Sort algorithm finds the lowest value in an array and 
    # moves it to the front of the array.
    for i in range(len(list) - 1):
        lowest_number_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[lowest_number_index]:
                lowest_number_index = j 
        if lowest_number_index != i:
            temp = list[i]
            list[i] = list[lowest_number_index]
            list[lowest_number_index] = temp
    return list

print(selection_sort([21, 1, 3, 7, 4, 9, 10, 7, 17, 5, 0, 100]))