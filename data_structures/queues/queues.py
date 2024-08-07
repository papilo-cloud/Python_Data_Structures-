class Queue:
    def __init__(self):
        self.data_store = []
            
    def enqueue(self, elem):
        self.data_store.append(elem)
    
    def dequeue(self):
        if self.data_store:
            return self.data_store.pop(0)
        return 'Cannot deque from an empty queue'
    
    def is_empty(self):
        if not self.data_store:
            return True
        
    def size(self):
        return len(self.data_store)
    
    def peek(self):
        if not self.is_empty():
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
