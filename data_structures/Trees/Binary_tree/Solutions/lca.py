# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def lca(root, alpha, beta):
    if not root:
        return
    if (root.val == alpha) or (root.val == beta):
        return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)
    
    if (left and right):
        return root
    else:
        if left:
            return left
        else:
            return right