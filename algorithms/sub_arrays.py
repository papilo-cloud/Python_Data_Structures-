def sub_array(arr, start, end):
    if end == len(arr):
        return
    if start > end:
        return sub_array(arr, 0, end+1)
    else:
        print(arr[start : end+1])
        return sub_array(arr, start+1, end)

sub_array([1,2,3], 0, 0)