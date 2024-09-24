# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def deepest_node(root):
    if not root:
        return
    
    q = []
    q.append(root)
    node = None
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return node.val