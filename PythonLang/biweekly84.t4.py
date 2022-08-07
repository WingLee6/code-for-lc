from typing import List, Optional
from Tools.operations_tree import operations_bi_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def test(self, a: int):
        print("Testing Solution")
        return False


if __name__ == '__main__':

    param = [2, 7, 11, 15]
    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root.val)

    solution = Solution()
    result = solution.test(a=param)
    print(result)
