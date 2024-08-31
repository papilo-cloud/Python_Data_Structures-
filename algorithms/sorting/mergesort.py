# The Merge Sort algorithm is a divide-and-conquer algorithm that sorts
# an array by first breaking it down into smaller arrays, and then building
# the array back together the correct way so that it is sorted.
def merge_ordered_lists(listA, listB):
    a = 0
    b = 0
    new_list = []
    
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            new_list.append(listA[a])
            a += 1
        else:
            new_list.append(listB[b])
            b += 1
    while a < len(listA):
        new_list.append(listA[a])
        a += 1
    while b < len(listB):
        new_list.append(listB[b])
        b += 1
    
    return new_list

def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    midpoint = len(the_list) // 2
    
    left_half = merge_sort(the_list[:midpoint])
    right_half = merge_sort(the_list[midpoint:])
    
    newlist = merge_ordered_lists(left_half, right_half)
    
    return newlist

arr = [10, 23, 51, 18, 4, 31, 13, 5, 65, 40]
print(merge_sort(arr))