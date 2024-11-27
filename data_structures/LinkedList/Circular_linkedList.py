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
    
    def delete(self, data):
        pass


llist = CircularList()

llist.append('hello')
llist.append('world')
llist.append('once')
llist.append('upon')
llist.append('a')
llist.append('time')

llist.print()