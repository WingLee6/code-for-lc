#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return headA if headA else headB

        pa = headA
        pb = headB

        seen = set()
        while pa and pb:
            if pa in seen:
                return pa
            else:
                seen.add(pa)
            if pb in seen:
                return pb
            else:
                seen.add(pb)

            pa = pa.next
            pb = pb.next

        pc = pa if pa else pb
        while pc:
            if pc in seen:
                return pc

            pc = pc.next

        return None


# @lc code=end
