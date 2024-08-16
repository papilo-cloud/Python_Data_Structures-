class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DbLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_head(self):
        current = self.head
        self.head = self.head.next
        return current.data
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
class Queues:
    def __init__(self) -> None:
        self.data = DbLinkedList()
    
    def enqueue(self, data):
        self.data.append(data)
    
    def dequeue(self):
        return self.data.remove_head()
    
    def print(self):
        return self.data.display()


queue = Queues()

queue.enqueue('hello')
queue.enqueue('once')
queue.enqueue('upon')
queue.enqueue('a')
queue.enqueue('time')

# queue.print()
print(queue.dequeue())
print(queue.dequeue())
