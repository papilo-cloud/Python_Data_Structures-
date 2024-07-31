def merge_sorted_list(listA, listB):
    newlist = []
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else :
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist

arr1 = [2, 8, 15, 23, 37]
arr2 = [4, 6, 15, 20]
print(merge_sorted_list(arr1, arr2))