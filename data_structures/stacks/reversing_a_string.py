import stack
def reversing_a_string(string):
    
    # I imported and used the already build Stack as a module
    lists = stack.Stack()
    reversed_string = ''
    
    for i in string:
        lists.push(i)
    while lists.length() > 0:
        reversed_string += lists.pop()
        
    return reversed_string

print(reversing_a_string('abcdef'))
    