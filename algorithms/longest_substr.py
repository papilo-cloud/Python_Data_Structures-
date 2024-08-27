
def longest_substr(arr):
    
    visited = [-1] * 256
    left = 0
    right = 0
    count = 0
    while right < len(arr):
        if visited[ord(arr[right])] != -1:
            left = max(visited[ord(arr[right])]+1, left)
        
        visited[ord(arr[right])] = right
        count = max(count, right - left + 1)
        right += 1
    return count 

arr = 'abcdbc'
print(longest_substr(arr))