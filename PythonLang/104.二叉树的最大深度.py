# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 11:57 PM
# @Author  : lee
# @FileName: q104_二叉树的最大深度.py
# @Desc    :

"""
104. 二叉树的最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional

from PythonLang.Tools.operations_tree import operations_bi_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _max_depth(self, root: Optional[TreeNode], depth) -> int:
        """方法一迭代法

        :param root:
        :param depth:
        :return:
        """
        if root:
            depth = 1 + max(self._max_depth(root=root.left, depth=depth), self._max_depth(root=root.right, depth=depth))

        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 方法一迭代法
        # return self._max_depth(root=root, depth=0)

        # 方法二层次遍历法
        if not root:
            return 0

        node_queue = [root]
        end_node = root
        depth = 1
        while node_queue:
            p = node_queue[0]
            node_queue.pop(0)
            if p.left:
                node_queue.append(p.left)
            if p.right:
                node_queue.append(p.right)

            if end_node == p and node_queue:
                end_node = node_queue[len(node_queue)-1]
                depth += 1

        return depth


if __name__ == '__main__':
    param = [28, 28, None, 50, 67, 88, 64, None, 53, 42, 60, 1, 42, None, 96, 76, 47, 6, 47, 19, 61, 95, 16, 86, 19, 93, 20, 82, 45, 23, 0, 7, 31, 21, None, 37, 64, 86, 8, 16, 58, 19, 84, 64, 7, 50, 57, 90, 84, 19, None, 33, None, 16, 96, None, 23, 29, 74, 35, 69, 91, 40, 15, 93, 5, 6, 95, 48, 32, 64, None, 65, 68, 58, 33, 74, 12, 60, 15, 84, 53, 10, 26, 32, 94, 32, 63, 56, 47, 87, 61, 28, 61, 26, None, 39, 95, 13, 46]


    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)

    solution = Solution()
    result = solution.maxDepth(root=tree.tree_root)
    print(result)

"""
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""

