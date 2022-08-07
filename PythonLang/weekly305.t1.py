import re
from typing import List, Optional
from Tools.operations_tree import operations_bi_tree

import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def test(self, nums: List[int], diff: int):

        return False

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        print("------")
        result = 0
        max_num = max(nums)

        for p in range(diff):
            tmp_result = 0
            n = 0
            tmp = []
            while p+n*diff <= max_num:
                if p+n*diff in nums:
                    tmp.append(p+n*diff)
                    tmp_result += 1
                    
                n += 1
            print(tmp)
            
            if tmp_result >= 3:
                # print(math.factorial(tmp_result)/(math.factorial(tmp_result-diff) * math.factorial(tmp_result)))

                print(math.factorial(tmp_result)//(math.factorial(diff)*math.factorial(tmp_result-diff)))
                result += tmp_result - diff + 1
                # result += math.factorial(tmp_result)//(math.factorial(diff)*math.factorial(tmp_result-diff))

                # result += math.factorial(tmp_result)/(math.factorial(tmp_result-diff) * math.factorial(tmp_result))
        

        print("------")

      

        return result


if __name__ == '__main__':

    param = [2, 7, 11, 15]
    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root.val)

    nums = [0, 1, 4, 6, 7,10]
    diff = 3

    solution = Solution()
    result = solution.arithmeticTriplets(nums=nums, diff=diff)
    print(result)

    from math import factorial
 

    print(4324242341412)
    # def CmbinationNumber(n,m):
    #     if m <= n:
            
    #         a=factorial(n)/(factorial(n-m) * factorial(m))
    #     return a
    
    # res = CmbinationNumber(4, 3)
    # print(res)
    n,m = 4,3
    r = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
    print(r)

