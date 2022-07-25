#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.post_order_visit = []


    def _post_order(self, root: Optional[TreeNode]):
        if root:
            self._post_order(root=root.left)
            self._post_order(root=root.right)
            self.post_order_visit.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self._post_order(root=root)
        return self.post_order_visit

# @lc code=end

