#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root  
        self.queue = []

        if root:
            p = root
            self.queue.append(p)
            while self.queue:
                p = self.queue[0]
                if p.left:
                    self.queue.append(p.left)
                if p.right:
                    self.queue.append(p.right)
                    self.queue.pop(0)
                if not (p.left and p.right):
                    break
                    
        
    def insert(self, val: int) -> int:
        q = TreeNode()
        q.val = val
        if not self.root:
            self.root = q
            self.queue.append(self.root)
            return None

        elif self.root:
            p = self.queue[0]
            if not p.left:
                p.left = q
                self.queue.append(p.left)
            elif not p.right:
                p.right = q
                self.queue.append(p.right)
                self.queue.pop(0)
        
            return p.val

    def get_root(self) -> TreeNode:
        return self.root


# @lc code=end

