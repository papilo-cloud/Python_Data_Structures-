class Queue:
    def __init__(self):
        self.data_store = []
    
    def enqueue(self, elem):
        self.data_store.append(elem)
    
    def dequeue(self):
        return self.data_store.pop(0)
        
    def size(self):
        return len(self.data_store)
    
    def is_empty(self):
        if len(self.data_store) == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.data_store[0]
        
queue = Queue()
