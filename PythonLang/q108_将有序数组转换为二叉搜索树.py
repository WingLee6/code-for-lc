# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 9:00 AM
# @Author  : lee
# @FileName: q108_将有序数组转换为二叉搜索树.py
# @Desc    :


""""
108. 将有序数组转换为二叉搜索树

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List, Optional

from PythonLang.Tools.operations_tree import operations_bi_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def _build_tree(left, right):
            # 递归出口
            if left > right:
                return None
            # 选择当前列表的根结点元素
            # 选择中间位置右边的数字作为根节点
            mid = (left + right + 1) // 2

            # 递归建立二叉树
            root = TreeNode(nums[mid])
            root.left = _build_tree(left, mid - 1)
            root.right = _build_tree(mid + 1, right)
            return root

        return _build_tree(0, len(nums) - 1)


if __name__ == '__main__':
    param = [-10,-3,0,5,9]

    s = Solution()
    result = s.sortedArrayToBST(param)
    print("------------------------")
    print(result)
    tree = operations_bi_tree()
    tree.level_order(root=result)
    print(tree.level_order_visit)

"""
示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
"""
