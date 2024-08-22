from collections import deque
class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

class Tree:
    def __init__(self) -> None:
        self.root_node = None
    
    # Insertion of a node in a BST takes O(h), where h is the height of the Tree.
    def insert(self, data):
        node = Node(data)
        if not self.root_node:
            self.root_node = node
        
        current = self.root_node
        parent = None
        while True:
            parent = current
            if node.data > current.data:
                current = current.right_child
                if not current:
                    parent.right_child = node
                    return
            else:
                current = current.left_child
                if not current:
                    parent.left_child = node
                    return
    def search(self, data):
        current = self.root_node
        while True:
            if not current:
                return None
            elif current.data == data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
                
    # Depth-first traversal
    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left_child)
        print(node.data)
        self.inorder_traversal(node.right_child)
    
    def preorder_traversal(self, node):
        if not node:
            return
        print(node.data)
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)
    
    # Breadth-first traversal
    def bf_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])

        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes
    
    def get_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data
    
    def get_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data
    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        
        if not current:
            return None
        while True:
            if current.data == data:
                return (parent, current.data)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
                
    # The remove operation takes O(h), where h is the height of the tree.
    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        self.size -= 1
        
        if not (parent and node):
            return False
        # Get children count
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (not node.left_child) and (not node.right_child):
            children_count = 0
        else:
            children_count = 1
        
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.right_child is node:
                    parent.right_child = next_node
                else:
                    parent.left_child = next_node
            else:
                self.root_node = next_node
        
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
        


tree = Tree()

tree.insert(50)
tree.insert(20)
tree.insert(70)