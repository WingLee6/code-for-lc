# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 12:08 AM
# @Author  : lee
# @FileName: q83_删除排序链表中的重复元素.py
# @Desc    :

"""
83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.next and p.val == p.next.val:
                p.next = p.next.next
            else:
               p = p.next
        return head




if __name__ == '__main__':
    param = [1,1,2]
    head = ListNode()
    head.val = param[0]
    head.next = None

    p = head
    for i in param[1:]:
        node = ListNode()
        node.val = i
        node.next = None
        p.next = node
        p = p.next

    solution = Solution()
    result = solution.deleteDuplicates(head=head)

    while result:
        print(result.val)
        result = result.next


"""
示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]
"""
