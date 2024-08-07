import stack
def postfix(arr):
    # Imported from the stack file
    stacks = stack.Stack()
    # stacks = []
    
    for i in arr:
        if i == '+':
            stacks.push(stacks.pop() + stacks.pop())
        elif i == '*':
            stacks.push(stacks.pop() * stacks.pop())
        elif i == '/':
            a = stacks.pop()
            b = stacks.pop()
            stacks.push(b / a)
        else:
            stacks.push(i)
    return stacks[0]

print(postfix([8, 2, 3, '+', '*', 4,'/', ]))