#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
from platform import node
from typing import Optional
from collections import deque

from idna import valid_contextj


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            add_node = TreeNode()
            add_node.val = val
            add_node.left = root
            root = add_node
            
            return root

        node_queue = deque([])  
        end_node = root
        node_queue.append(end_node)
        level = 1
        while node_queue and level != depth-1:
            p = node_queue.popleft()
            if p.left:
                node_queue.append(p.left)
            if p.right:
                node_queue.append(p.right)

            if p == end_node:
                end_node = node_queue[len(node_queue)-1]
                level += 1
            
        
        while node_queue:
            q = node_queue.popleft()
            
            tmp_left_node = q.left
            tmp_right_node = q.right
            
            add_left_node = TreeNode()
            add_left_node.val = val
            add_right_node = TreeNode()
            add_right_node.val = val
            
            q.left = add_left_node
            q.left.left = tmp_left_node
            q.right = add_right_node
            q.right.right = tmp_right_node
                
        return root
                    


# @lc code=end


"""
input:
[4,2,6,3,1,5]
1
1
output:
[1,4,null,2,6,3,1,5]
"""