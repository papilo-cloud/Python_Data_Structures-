class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class DbLinkedList:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def display(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next
    
    def remove_from_head(self):
        removed_node = self.head.data
        self.head.previous = None
        self.head = self.head.next
        return removed_node
    
    def delete(self, data):
        current_node = self.head
        # node_deleted = False
        if not current_node:
            return False
        elif current_node.data == data:
            current_node = current_node.next
            current_node.previous = None
            return True
        elif self.tail.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            return True
        else:
            while current_node:
                if current_node.data == data:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    return True
                current_node = current_node.next
                
    def reverse(self):
        # By swapping positions
        # current = self.head
        # tempt = None
        # while current:
        #     tempt = current.previous
        #     current.previous = current.next
        #     current.next = tempt
        #     current = current.previous
        # if tempt:
        #     self.head = tempt.previous

        # By using stack -- My favorite --
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
            
        current = self.head
        while current:
            current.data = stack[-1]
            stack.pop()
            current = current.next
    
    def display_reversed(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.previous
    def find_last(self):
        return self.tail.data
            
        
    

llist = DbLinkedList()
llist.append('hello')
llist.append('once')
llist.append('upon')
llist.append('a')
llist.append('time')
llist.display()
# print(llist.find_last())
print(' ')
llist.display_reversed()