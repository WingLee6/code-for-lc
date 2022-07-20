# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 12:15 AM
# @Author  : lee
# @FileName: operations_tree.py
# @Desc    : 树的基本操作


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.node_queue = []


class operations_bi_tree:
    """二叉树的基本操作

    方法：
    leetcode_level_build_tree:  [LeetCode特殊层次遍历序列] 转 [二叉树]
    pre_order:                  前序遍历二叉树
    in_order:                   中序遍历二叉树
    post_order:                 后序遍历二叉树


    Attributes:
        tree_root: None或TreeNode类型，树的根结点（即，二叉树），默认为空树None
        pre_order_visit: 列表，表示二叉树的前序遍历序列
        in_order_visit: 列表，表示二叉树的中序遍历序列
        post_order_visit: 列表，表示二叉树的后序遍历序列
        level_order_visit: 列表，表示二叉树的层次遍历序列
    """
    def __init__(self):
        self.tree_root = None
        self.pre_order_visit = []
        self.in_order_visit = []
        self.post_order_visit = []
        self.level_order_visit = []

    def leetcode_level_build_tree(self, tree_val: List[int]) -> Optional[TreeNode]:
        """[LeetCode特殊层次遍历序列] 转 [二叉树]

        [LeetCode特殊层次遍历序列]的具体格式：https://support.leetcode.cn/hc/kb/article/1567641/

        :param tree_val: 一个列表，列表元素表示树结点的值，格式见上述链接
        :return:
        """

        def _add_treenode():
            """增加孩子结点和叶子结点

            利用队列完成二叉树的建立

            :return:
            """
            p = node_queue[0]
            node_queue.pop(0)
            if p:
                t_left = None
                t_right = None
                if tree_val and tree_val[0] is not None:
                    t_left = TreeNode()
                    t_left.val = tree_val[0]
                    tree_val.pop(0)
                elif tree_val:
                    tree_val.pop(0)

                if tree_val and tree_val[0] is not None:
                    t_right = TreeNode()
                    t_right.val = tree_val[0]
                    tree_val.pop(0)
                elif tree_val:
                    tree_val.pop(0)

                p.left = t_left
                p.right = t_right
                node_queue.append(t_left)
                node_queue.append(t_right)

        # 若为空列表，返回空树
        if not tree_val:
            return None

        # 若为非空列表，初始化树的根结点
        self.tree_root = TreeNode()
        self.tree_root.val = tree_val[0]
        tree_val.pop(0)
        # 初始化队列，存放树的结点
        node_queue = [self.tree_root]

        # 循环增加分支结点，直至队列为空
        while node_queue:
            _add_treenode()
            # print("-------self.node_queue--------")
            # for i in self.node_queue:
            #     if i:
            #         print(i.val)
            #     else:
            #         print(i)
            # print("------------------")
            
    def pre_order(self, root: Optional[TreeNode]):
        """前序遍历二叉树

        递归实现前序遍历二叉树

        :param root: None或Optional[TreeNode]类型，树的根结点（即，二叉树），默认为空树None
        :return:
        """

        if root:
            self.pre_order_visit.append(root.val)
            self.pre_order(root=root.left)
            self.pre_order(root=root.right)

    def in_order(self, root: Optional[TreeNode]):
        """中序遍历二叉树

        递归实现中序遍历二叉树

        :param root: None或Optional[TreeNode]类型，树的根结点（即，二叉树），默认为空树None
        :return:
        """

        if root:
            self.in_order(root=root.left)
            self.in_order_visit.append(root.val)
            self.in_order(root=root.right)

    def post_order(self, root: Optional[TreeNode]):
        """后序遍历二叉树

        递归实现后序遍历二叉树

        :param root: None或Optional[TreeNode]类型，树的根结点（即，二叉树），默认为空树None
        :return:
        """

        if root:
            self.post_order(root=root.left)
            self.post_order(root=root.right)
            self.post_order_visit.append(root.val)

    def level_order(self, root: Optional[TreeNode]):
        """层次遍历二叉树

        队列实现层次遍历二叉树

        :param root: None或Optional[TreeNode]类型，树的根结点（即，二叉树），默认为空树None
        :return:
        """
        if not root:
            return 0

        node_queue = [root]
        while node_queue:
            p = node_queue[0]
            node_queue.pop(0)
            if p.left:
                node_queue.append(p.left)
            if p.right:
                node_queue.append(p.right)

            self.level_order_visit.append(p.val)

    def max_depth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        """迭代法实现求二叉树的深度

        本例为迭代实现
        队列实现法见leetcode第104题

        :param root:
        :param depth:
        :return:
        """
        if root:
            depth = 1 + max(self.max_depth(root=root.left, depth=depth), self.max_depth(root=root.right, depth=depth))

        return depth

    # @max_depth(root=tree_root)
    def print_tree(self, root: Optional[TreeNode]):
        """ 打印树

        例如
        [3,9,20,null,null,15,7]
            3
           / \
          9  20
            /  \
           15   7
        :return:
        """


if __name__ == '__main__':
    root_list = [3, 9, 20, None, None, 15, 7]
    # root_list = [1, None, 2, 3]
    # root_list = [1]
    # root_list = []
    # root_list = [1, 2, 3, 4, None, 5, 6, None, None, None, 7, 8, None]

    root = operations_bi_tree()
    root.leetcode_level_build_tree(tree_val=root_list)

    # root.in_order(root=root.tree_root)
    # print(root.in_order_visit)
    #
    # root.pre_order(root=root.tree_root)
    # print(root.pre_order_visit)
    #
    # root.post_order(root=root.tree_root)
    # print(root.post_order_visit)
    #
    # root.level_order(root=root.tree_root)
    # print(root.level_order_visit)

    d = root.max_depth(root=root.tree_root)
    print(d)




"""
示例1：
输入：
[28, 28, null, 50, 67, 88, 64, null, 53, 42, 60, 1, 42, null, 96, 76, 47, 6, 47, 19, 61, 95, 16, 86, 19, 93, 20, 82, 45, 23, 0, 7, 31, 21, null, 37, 64, 86, 8, 16, 58, 19, 84, 64, 7, 50, 57, 90, 84, 19, null, 33, null, 16, 96, null, 23, 29, 74, 35, 69, 91, 40, 15, 93, 5, 6, 95, 48, 32, 64, null, 65, 68, 58, 33, 74, 12, 60, 15, 84, 53, 10, 26, 32, 94, 32, 63, 56, 47, 87, 61, 28, 61, 26, null, 39, 95, 13, 46]
[28, 28, None, 50, 67, 88, 64, None, 53, 42, 60, 1, 42, None, 96, 76, 47, 6, 47, 19, 61, 95, 16, 86, 19, 93, 20, 82, 45, 23, 0, 7, 31, 21, None, 37, 64, 86, 8, 16, 58, 19, 84, 64, 7, 50, 57, 90, 84, 19, None, 33, None, 16, 96, None, 23, 29, 74, 35, 69, 91, 40, 15, 93, 5, 6, 95, 48, 32, 64, None, 65, 68, 58, 33, 74, 12, 60, 15, 84, 53, 10, 26, 32, 94, 32, 63, 56, 47, 87, 61, 28, 61, 26, None, 39, 95, 13, 46]


输出：
中序遍历：
[26,50,32,93,94,57,32,76,63,90,56,20,47,84,87,42,61,19,28,82,47,61,33,26,45,88,16,39,23,95,96,13,6,0,46,23,60,29,7,74,47,35,31,69,50,91,21,40,19,1,15,37,93,61,5,64,6,64,95,86,48,95,32,8,64,42,16,65,16,68,58,58,28,67,53,33,19,74,86,12,84,60,96,15,64,84,19,53,7,10,28]


示例2：
输入：
[1,2,3,4,None,5,6,None,None,None,7,8,None]
输出：
中序：
[4, 2, 1, 5, 7, 3, 8, 6]
"""
