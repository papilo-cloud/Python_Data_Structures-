def select_even(array, index = 0):
    if len(array) == index:
       return []

    if array[index]%2 == 0:
        return [array[index]] + select_even(array, index + 1)
    return select_even(array, index + 1)

print(select_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))