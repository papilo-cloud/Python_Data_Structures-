def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    min_height = 0
    while left < len(height):
        
        if height[left] > height[right]:
            min_height = height[right]
        else:
            min_height = height[left]
        max_area = max(max_area, (right - left)*min_height)
        
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
arr = [1,8,6,2,5,4,8,3,7]
print(max_area(arr))