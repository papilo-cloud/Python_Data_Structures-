def binary_search(list, search_value):
    lower_bound = 0
    upper_bound = len(list) - 1
    steps = 0
    
    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = list[midpoint]
        steps += 1
        
        if value_at_midpoint == search_value:
            print(f"steps: {steps}")
            return f'found at index: {midpoint}'
        elif value_at_midpoint > search_value:
            upper_bound = midpoint - 1
        elif value_at_midpoint < search_value:
            lower_bound = midpoint + 1
    print(f"steps: {steps}")
    return 'Not found'

print(binary_search([x for x in range(100)], 10))