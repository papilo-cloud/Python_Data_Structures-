# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def are_mirror(root1, root2):
    if (not root1) and (not root2):
        return True
    
    if (not root1) or (not root2):
        return False
    if root1.val != root2.val:
        return False
    left = are_mirror(root1.left, root2.left) and are_mirror(root1.right, root2.right)
    right = are_mirror(root1.left, root2.right) and are_mirror(root1.right, root2.left)
    
    if left or right:
        return True
    else:
        return False