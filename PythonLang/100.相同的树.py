# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 12:15 AM
# @Author  : lee
# @FileName: q100_相同的树.py
# @Desc    :


# Definition for a binary tree node.
from PythonLang.Tools.operations_tree import operations_bi_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p=p.left, q=q.left) and self.isSameTree(p=p.right, q=q.right)
        if not p and not q:
            return True

        return False


if __name__ == '__main__':
    print("dedde")
    p_list = [1, 2, 1]
    p = operations_bi_tree()
    p.leetcode_level_build_tree(tree_val=p_list)

    q_list = [1, 1, 2]
    q = operations_bi_tree()
    q.leetcode_level_build_tree(tree_val=q_list)

    solution = Solution()
    result = solution.isSameTree(p=p.tree_root, q=q.tree_root)
    print(result)


"""
示例 1: 
输入: p = [1,2,3], q = [1,2,3]
输出: true

示例 2: 
输入: p = [1,2], q = [1,null,2]
输出: false

示例 3: 
输入: p = [1,2,1], q = [1,1,2]
输出: false

"""
