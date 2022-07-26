#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归算法
        if not root:
            return None

        tmp_tree = TreeNode()
        tmp_tree = self.invertTree(root=root.left)
        root.left = self.invertTree(root=root.right)
        root.right = tmp_tree
            
        return root


# @lc code=end
