# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 12:02 AM
# @Author  : lee
# @FileName: q94_二叉树的中序遍历.py
# @Desc    :


"""
94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List, Optional
from PythonLang.Tools.BasicOperationsTreeNode import optional_tree as OT

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order(self, root: Optional[TreeNode], visit: List[int]) -> List[int]:
        if root:
            self.in_order(root=root.left, visit=visit)
            visit.append(root.val)
            self.in_order(root=root.right, visit=visit)
        return visit

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.in_order(root=root, visit=[])


if __name__ == '__main__':
    root_list = [1, None, 2, 3]
    root = OT()
    root.leetcode_level_build_tree(tree_val=root_list)

    solution = Solution()
    result = solution.inorderTraversal(root=root.t_root)
    print(result)

"""
示例 1：
输入：root = [1, None, 2, 3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
"""
