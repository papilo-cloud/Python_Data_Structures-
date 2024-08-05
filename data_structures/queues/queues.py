class Queue:
    def __init__(self):
        self.data_store = []
        self.size = 0
    
    def enqueue(self, elem):
        self.data_store.append(elem)
        self.size += 1
    
    def dequeue(self):
        self.size -= 1
        return self.data_store.pop(0)
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.data_store[0]
    def to_string(self):
        to_str = ''
        for i in self.data_store:
            to_str += i + "\n"
        return to_str
        
queue = Queue()

print(queue.size)
queue.enqueue('apple')
queue.enqueue('banana')
queue.enqueue('mango')
print(queue.size)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.to_string())
