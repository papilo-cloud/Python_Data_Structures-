class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class CircularList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.tail.next = self.head
    
    def print_list(self):
        current = self.head
        if current:
            print(current.data)
            current = current.next
        while current != self.head:
            print(current.data)
            current = current.next
    
    def delete(self, data):
        current = self.head
        prev = self.head
        
        while prev == current or prev != self.tail:
            if current.data == data:
                if current.data == self.head:
                    self.head = current.next
                    self.head.next = self.head
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next


llist = CircularList()

llist.append('hello')
llist.append('world')
llist.append('once')
llist.append('upon')
llist.append('a')
llist.append('time')

llist.print()