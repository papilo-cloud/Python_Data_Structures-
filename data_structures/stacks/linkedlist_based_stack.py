class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, elem):
        newnode = Node(elem)
        newnode.next = self.head
        self.head = newnode
       
    def pop(self):
        if not self.head:
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def peek(self):
        if not self.head:
            raise IndexError
        return self.head.data