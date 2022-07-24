#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:

    def __init__(self, head):
        self.nodes = []   
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self):  
        return random.choice(self.nodes)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

