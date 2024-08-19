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
    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left_child)
        print(node.data)
        self.inorder_traversal(node.right_child)
        


tree = Tree()

tree.insert(50)
tree.insert(20)
tree.insert(70)