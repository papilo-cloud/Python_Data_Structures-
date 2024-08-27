arr = [1, 2, 3, 4, 5]

def two_pointers(list, k):
    left = 0
    right = len(list) - 1
    while left <= len(list)//2:
        if list[left] + list[right] is k:
            return [left, right]
        elif list[left] + list[right] < k:
            left += 1
        else:
            right -= 1
    return False

print(two_pointers(arr, 8))