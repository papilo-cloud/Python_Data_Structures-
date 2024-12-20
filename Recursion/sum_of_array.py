def sum(array):
    if not array:
        return 0
    return array[0] + sum(array[1:])

print(sum([1, 2, 3, 4, 5]))