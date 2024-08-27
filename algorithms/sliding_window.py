arr = [5, 3, 1, 9, 5]


def sliding_window(arr, k):
    # Explanation:
    # Start with the sum of the first k elements.
    # Slide the window one element at a time, subtracting the element that goes out of the window and adding the new element.
    # Keep track of the maximum sum encountered.
    
    n = len(arr)
    if n < k:
        return 
    windows = sum(arr[:k])
    max_sum = windows
    
    for i in range(n - k):
        windows = windows - arr[i] + arr[i + k]
        max_sum = max(max_sum, windows)
    return max_sum

print(sliding_window(arr, 2))