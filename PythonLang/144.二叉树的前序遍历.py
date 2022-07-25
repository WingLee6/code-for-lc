#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
import re
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre_order_visit = []


    def _pre_order(self, root: Optional[TreeNode]):
        """前序遍历二叉树

        递归实现前序遍历二叉树

        :param root: None或Optional[TreeNode]类型，树的根结点（即，二叉树），默认为空树None
        :return:
        """

        if root:
            self.pre_order_visit.append(root.val)
            self._pre_order(root=root.left)
            self._pre_order(root=root.right)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self._pre_order(root=root)
        return self.pre_order_visit


# @lc code=end

