# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_size(root):
    if not root:
        return
    
    q = []
    q.append(root)
    size = 0
    
    while q:
        node = q.pop(0)
        size += 1
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return size