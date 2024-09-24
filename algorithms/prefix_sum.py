arr = [1, 2, 3, 4, 5, 6]

def prefix_sum(list):
    prefix = [0 for i in range(len(list))]
    prefix[0] = list[0]
    for i in range(len(list)):
        prefix[i] = prefix[i - 1] + list[i]
    return prefix

print(prefix_sum(arr))

def longest_sub_arr(arr, k):
    prefix = max_len = 0
    mpp = {}
    
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == k:
            max_len = max(max_len, i + 1)
        x = prefix - k
        if x in  mpp:
            ln = i - mpp[x]
            max_len = max(max_len, ln)
        
        if prefix not in mpp:
            mpp[prefix] = 1
    print(mpp)
    print(max_len)
x = [1,2,3]
k = 3
longest_sub_arr(x, k)