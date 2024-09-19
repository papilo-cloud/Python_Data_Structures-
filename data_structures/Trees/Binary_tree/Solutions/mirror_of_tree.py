# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
    return root