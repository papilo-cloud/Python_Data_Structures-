# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def number_of_leaves(root):
    if not root:
        return
    
    q = []
    q.append(root)
    count = 0
    
    while q:
        node = q.pop(0)
        if (not node.left) and (not node.right):
            count += 1
        else:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return count