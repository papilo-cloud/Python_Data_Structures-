class Stack:
    def __init__(self):
        self.data_store = []
    
    def push(self, element):
        self.data_store.append(element)
        
    def pop(self):
        if (len(self.data_store) == 0):
            return False
        else:
            return self.data_store.pop()
    
    def peek(self):
        if (len(self.data_store) == 0):
            return 'No element in the Stack'
        else:
            return self.data_store[len(self.data_store) - 1]
    
    def length(self):
        return len(self.data_store)
    
    def last(self):
        if len(self.data_store) == 1:
            return self.data_store[len(self.data_store) - 1]
        else:
            return False
    
# NOTE: Uncommenting this part of the code will affect the other files where it is imported as a module
# stack = Stack()

# stack.push('Hello')
# stack.push('Hi')
# stack.push('Bonjour')
# stack.push('Merci')

# print(stack.length())
# print(stack.peek())

# stack.pop()
# print(stack.length())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.last())