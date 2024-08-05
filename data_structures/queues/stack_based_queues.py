class QeueuWithStacks:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []
        self.size = 0
    
    def enqueue(self, elem):
        self.inbound_stack.append(elem)
        self.size += 1
    
    def dequeue(self):
        if self.inbound_stack:
            self.outbound_stack.append(self.inbound_stack.pop(0))
            self.size -= 1
        self.outbound_stack.pop()
    
    def peek(self):
        if not self.size:
            return False
        else:
            return self.inbound_stack[0]
        
        
queue = QeueuWithStacks()

# Queries
q = int(input())
for i in range(q):
    type = input().split()
    if type[0] == '1':
        queue.enqueue(type[1])
    elif type[0] == '2':
        queue.dequeue()
    else:
        print(queue.peek())
