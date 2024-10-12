import stack

def number_base_conversion(number, base):
    
    lists = stack.Stack()
    converted_number = ''
    
    while number > 0:
        remainder = number%base
        lists.push(str(remainder))
        number = (number // base)
        
    while lists.length() > 0:
        converted_number += lists.pop()
    return converted_number

print(number_base_conversion(32, 2))
print(number_base_conversion(32, 8))
print(number_base_conversion(32, 16))
