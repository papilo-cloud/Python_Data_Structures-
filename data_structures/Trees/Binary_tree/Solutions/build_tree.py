class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def build_tree(self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1: 1 + root_pos], inorder[: root_pos])
        root.right = self.build_tree(preorder[root_pos + 1:], inorder[root_pos + 1:])
        return root