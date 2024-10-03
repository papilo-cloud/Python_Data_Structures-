class BinartTree:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None
    
    def set_data(self, data):
        self.val = data
    
    def get_data(self):
        return self.val
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def preorder(self, root, result=[]):
        if not root:
            return
        stk = []
        stk.append(root)
        while stk:
            node = stk.pop()
            result.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        return result 
    
    def inorder(self, root, result=[]):
        if not root:
            return
        
        stk = []
        node = root
        
        while node or stk:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                result.append(node.val)
                node = node.right
        return result
    
    def postorder(self, root, result=[]):
        if not root:
            return
        
        visited = {}
        stk = []
        node = root
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                if node.right and not node.right in visited:
                    stk.append(node)
                    node = node.right
                else:
                    visited[node] = 1
                    result.append(node.val)
                    node = None
        return result