def counting_sort(arr):
    # The Counting Sort algorithm sorts an array by counting the number 
    # of times each value occurs.
    m = max(arr)
    freq = [0 for i in range(m+1)]
    print(freq)
    for j in arr:
        freq[j] += 1
    
    result = []
    i = 0
    while i < len(freq):
        if i in arr:
            j = 0
            while j < freq[i]:
                result.append(i)
                j += 1
        i += 1
    return result
x = [1,1,3,2,1]
print(counting_sort(x))