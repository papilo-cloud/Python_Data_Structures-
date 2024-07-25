import stack

def factorials(number):
    # I imported and used the already build Stack as a module
    lists = stack.Stack()
    answer = 1
    
    for i in range (1, number + 1):
        lists.push(i)
    
    while lists.length() > 0:
        answer *= lists.pop()
    return answer

print(factorials(6))
    