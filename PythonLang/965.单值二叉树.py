#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if not root:
            return 0

        level_order_visit = []
        node_queue = [root]

        while node_queue:
            p = node_queue[0]
            node_queue.pop(0)
            if p.left:
                node_queue.append(p.left)
            if p.right:
                node_queue.append(p.right)
            if level_order_visit and not p.val in level_order_visit:
                return False
            level_order_visit.append(p.val)

        return True

# @lc code=end

