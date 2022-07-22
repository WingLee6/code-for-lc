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

    dp = [[0]* len([7,1,5,3,6,4]))] * 3
    for input in range(len([7,1,5,3,6,4])-1):
    # print(input)
        for output in range(input+1, len([7,1,5,3,6,4])):
            print(output)
        print('---------------')




    

    