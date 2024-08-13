class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def insert(self, data):
        new_node = Node(data)
        self.size += 1
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next
            current_index += 1
        new_node.next = current_node.next
        current_node.next = new_node
    
    def read(self, index):
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node.data
    
    def index_of(self, value):
        current_node = self.head
        current_index = 0
        
        while current_node:
            if current_node.data == value:
                return current_index
            else:
                current_node = current_node.next
                current_index += 1
        return False
    
    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next
            current_index += 1
        node_index = current_node.next.next
        current_node.next = node_index

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def reversed(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            
            prev = current
            current = new_node
        self.head = prev

llist = LinkedList()

llist.insert('hello')
llist.insert('world')
llist.insert('once')
llist.insert('upon')
# llist.insert('a')
# llist.insert('time')
# llist.delete_at_index(2)
# llist.insert_at_index('goodmorning', 2)
llist.display()

# print(llist.search('world'))