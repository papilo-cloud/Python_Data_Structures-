# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def delete_binary_tree(root):
    if not root:
        return
    delete_binary_tree(root.left)
    delete_binary_tree(root.right)
    del root