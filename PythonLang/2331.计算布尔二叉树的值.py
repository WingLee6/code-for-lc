#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val in [0, 1]:
            if root.val == 0:
                return False
            else:
                return True
        if root.val in [2, 3]:
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            else:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)

# @lc code=end
