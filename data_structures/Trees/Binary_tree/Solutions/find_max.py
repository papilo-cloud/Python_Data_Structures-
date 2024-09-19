# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using Recursion
max_data = float('-infinity')
def find_max(root):
    global max_data
    if not root:
        return max_data
    if root.val > max_data:
        max_data = root.val
    find_max(root.left)
    find_max(root.right)
    return max_data


# Without Recursion
def find_max(root):
    if not root:
        return
    q = []
    q.append(root)
    max_data = 0
    
    while q:
        node = q.pop
        if max_data > node.val:
            max_data = node.val
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return max_data