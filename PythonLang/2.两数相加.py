# -*- coding: utf-8 -*-
# @Time     : 2022/3/5
# @Author   : lee
# @FileName : q2_addTwoNumbers.py
# @Desc     : LeetCode Q2 两数相加


"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import PythonLang.Tools.operations_node as BasicOperations

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        两数相加
        :param l1:
        :param l2:
        :return:
        """
        result_listNode = ListNode(l1.val + l2.val)
        rt, tp = result_listNode, result_listNode
        while (l1 and (l1.next != None)) or (l2 and (l2.next != None)) or (tp.val > 9):
            l1 = l1.next if l1 else l1              # 如果l1（if后的判断）存在则l1=l1.next，否则l1=l1
            l2 = l2.next if l2 else l2

            tmp_sum_int = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tp.next = ListNode(tp.val // 10 + tmp_sum_int)
            tp.val %= 10
            tp = tp.next
        return rt


# 主函数
if __name__ == "__main__":
    # Step1: 构建两个测试链表，不带头结点
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]
    l1_listNode = BasicOperations.LinkList().initTailInsert(data=l1_list)
    l2_listNode = BasicOperations.LinkList().initTailInsert(data=l2_list)

    # Step2. 将链表带入算法
    result_listNode = Solution().addTwoNumbers(l1=l1_listNode, l2=l2_listNode)
    BasicOperations.LinkList().travelList(result_listNode)
