class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
    def is_empty(self):
        if not self.queue:
            return True
    def size(self):
        return len(self.queue)
    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        self.queue.append(entry)
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        
    def dequeue(self):
        if self.queue:
            highest = self.queue[0]
            indexof_item = self.queue.index(highest)
            for item in self.queue:
                if item.priority < highest.priority:
                    highest = item
                    indexof_item = self.queue.index(item)
            entry = self.queue.pop(indexof_item)
            return entry.item
        return 'Cannot deque from an empty queue'
    
    
class PriorityQEntry:
    def __init__(self, item, priority) -> None:
        self.item = item
        self.priority = priority
        
        
queue = PriorityQueue()
queue.enqueue('hello', 2)
queue.enqueue('bonjour', 3)
queue.enqueue('morning', 2)
queue.enqueue('sannu', 4)
queue.enqueue('good', 1)
print('size',queue.size())

print(f'first item is: {queue.peek().item}')
print(f'dequeued first priority {queue.dequeue()}')

print('size',queue.size())
