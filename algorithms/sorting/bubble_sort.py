def bubble_sort(list):
    # Bubble Sort is an algorithm that sorts an array from the lowest
    # value to the highest value.

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                sorted = False
                
    return list

print(bubble_sort([2, 1, 3, 7, 4, 9, 0, 7]))