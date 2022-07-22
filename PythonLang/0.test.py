from typing import List, Optional
from Tools.operations_node import ListNode
from Tools.operations_tree import operations_bi_tree


class Solution:
    def test(self, a: int):
        
        return False



if __name__ == '__main__':
    param = [2, 7, 11, 15]


    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root)
    
    solution = Solution()
    result = solution.test(a=param)
    print(result)
    

    