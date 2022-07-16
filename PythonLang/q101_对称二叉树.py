# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 8:03 PM
# @Author  : lee
# @FileName: q101_对称二叉树.py
# @Desc    :


"""
101. 对称二叉树

给你一个二叉树的根节点 root ， 检查它是否轴对称。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional
from PythonLang.Tools.operations_tree import operations_bi_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_left_and_right(self, left_tree: Optional[TreeNode], right_tree: Optional[TreeNode]) -> bool:

        if not left_tree and not right_tree:
            return True
        if left_tree and right_tree:
            if left_tree.val == right_tree.val:
                return self._is_left_and_right(left_tree=left_tree.left, right_tree=right_tree.right) \
                       and self._is_left_and_right(left_tree=left_tree.right, right_tree=right_tree.left)

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._is_left_and_right(left_tree=root.left, right_tree=root.right)


if __name__ == '__main__':
    param = [1, 2, 3]

    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)

    solution = Solution()
    result = solution.isSymmetric(root=tree.tree_root)
    print(result)



"""
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1, 2, 2, None, 3, None, 3]
输出：false

示例 3：
输入：root = [1, 2, 3]
输出：false

"""
