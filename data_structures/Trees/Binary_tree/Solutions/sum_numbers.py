# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sum_numbers(root):
    if not root:
        return 0
    current = 0
    summ = [0]
    cal_sum(root, current, summ)
    return summ[0]

def cal_sum(root, current, summ):
    if not root:
        return
    current = current*10 + root.val
    if not root.left and not root.right:
        summ[0] += current
        return
    cal_sum(root.left, current, summ)
    cal_sum(root.right, current, summ)