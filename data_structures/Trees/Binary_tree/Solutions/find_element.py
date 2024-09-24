# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_elem(root, data):
    if not root:
        return False
    
    q = []
    q.append(root)
    
    while q:
        node = q.pop(0)
        if data == node.val:
            return True
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return False