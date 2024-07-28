def binary_search(array, search_val, upper_bound, lower_bound = 0):
    if lower_bound > upper_bound:
        return 'Not found'
    else:
        midpoint = (lower_bound + upper_bound) // 2
        midpoint_val = array[midpoint]
        
        if midpoint_val == search_val:
            return midpoint
        if midpoint_val > search_val:
            return binary_search(array, search_val, midpoint - 1, lower_bound)
        if midpoint_val < search_val:
            return binary_search(array, search_val, upper_bound, midpoint + 1)

array = [2, 7, 19, 34, 53, 72]
print(binary_search(array, 53, len(array) - 1))