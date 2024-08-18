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
        else:
            current = self.root_node
            if node.data > current.data:
                if not current.right_child:
                    current.right_child = node
                else:
                    self.insert(node)
            else:
                if not self.root_node.data:
                    self.root_node.left_child = node
                else:
                    self.insert(node)


tree = Tree()

tree.insert(50)
tree.insert(20)
tree.insert(70)