def sum(array, index = 1):
    if len(array) == index:
        return array[0]
    return array[index] + sum(array, index + 1)

print(sum([1, 2, 3, 4, 5]))