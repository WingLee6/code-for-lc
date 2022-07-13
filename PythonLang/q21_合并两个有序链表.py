# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 8:58 AM
# @Author  : lee
# @FileName: q21_合并两个有序链表.py
# @Desc    :

"""
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        # 有个游标，标识 结果链表 的结尾
        move = dummy
        # l1 和 l2 都未遍历结束
        while list1 and list2:
            # 如果 l1 的数值比较小
            if list1.val <= list2.val:
                # 把 l1 头部节点拼接到 结果链表 的结尾
                move.next = list1
                # l1 指向下一个节点
                list1 = list1.next
            else:
                # 把 l2 头部节点拼接到 结果链表 的结尾
                move.next = list2
                # l2 指向下一个节点
                list2 = list2.next
            # 移动 结果链表 的结尾指针
            move = move.next
        # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        move.next = list1 if list1 else list2
        # 返回哑节点的下一个位置
        return dummy.next



if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4, 9]
    # l1 = [5]
    # l2 = [1, 2, 4]
    list1 = ListNode()
    list1.val = l1[0]
    list1.next = None

    p = list1
    for i in l1[1:]:
        node = ListNode()
        node.val = i
        node.next = None
        p.next = node
        p = p.next


    list2 = ListNode()
    list2.val = l2[0]
    list2.next = None

    p = list2
    for i in l2[1:]:
        node = ListNode()
        node.val = i
        node.next = None
        p.next = node
        p = p.next

    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)

    l = []
    while result:
        l.append(result.val)
        # print(result.val)
        result = result.next

    print(l)


"""
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

示例 4：
输入：
    l1 = [1,2,4]
    l2 = [1,3,4, 9]
输出：[1,1,2,3,4,4,9]

示例 5：
输入：
[5]
[1,2,4]
预期结果：
[1,2,4,5]
    

"""