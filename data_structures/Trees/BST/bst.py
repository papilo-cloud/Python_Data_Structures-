from collections import deque
class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

class Tree:
    def __init__(self) -> None:
        self.root_node = None
        self.hd = 0 # horizontal distance
    
    # Insertion of a node in a BST takes O(h), where h is the height of the Tree.
    def insert(self, data):
        node = Node(data)
        if not self.root_node:
            self.root_node = node
        else:
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
    
    def lowest_common_ancestor(self, root, n1, n2):
        current = root
        if not current:
            return None
        if (current.data > n1 and current.data > n2):
            return self.lca(current.left_child, n1, n2)
        
        if (current.data < n1 and current.data < n2):
            return self.lca(current.right_child, n1, n2)
        return current.data
    
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
    
    def top_view(self, root):
        if not root:
            return
        
        queue = []
        hash_table = {}
        hd = 0 # horizontal distance.
        root.hd = hd
        queue.append(root)
        
        while queue:
            root = queue[0]
            hd = root.hd
            
            if hd not in hash_table:
                hash_table[hd] = root.data 
            if root.left:
                root.left.hd = hd - 1
                queue.append(root.left)
            if root.right:
                root.right.hd = hd + 1
                queue.append(root.right)
            queue.pop(0)
        for i in sorted(hash_table):
            print(hash_table[i], end=' ')
    
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
        self.remove_node(self.root_node, data)
    
    def remove_node(self, node, value):
        if not node:
            return None
        if node.data == value:
            if not node.left_child:
                return node.right_child
            elif not node.right_child:
                return node.left_child
            else:
                current = self.get_smallest(node.right_child)
                node.data = current.data
                node.right_child = self.remove_node(node.right_child, current.data)
                return node
        elif node.data > value:
            node.left_child = self.remove_node(node.left_child, value)
            return node
        else:
            node.right_child = self.remove_node(node.right_child, value)
            return node
    
    def get_smallest(self, node):
        while node.left_child:
            node = node.left_child
        return node
        


tree = Tree()

tree.insert(50)
tree.insert(20)
tree.insert(70)