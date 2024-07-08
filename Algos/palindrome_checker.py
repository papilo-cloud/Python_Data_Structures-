def is_palindrome(str):
    left_index = 0
    right_index = len(str) - 1
    
    while left_index < (len(str) / 2):
        if str[left_index] != str[right_index]:
            return False
        left_index += 1
        right_index -= 1
        
    return True

print(is_palindrome('2022'))