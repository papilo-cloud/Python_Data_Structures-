def sub_array(arr, start, end):
    if end == len(arr):
        return
    if start > end:
        return sub_array(arr, 0, end+1)
    else:
        print(arr[start : end+1])
        return sub_array(arr, start+1, end)

def sub_array1(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            res.append(arr[i: j+1])
    return res
    

sub_array([1,2,3], 0, 0)