from collections import Counter
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

    
    nums = [1,2,3,4,5]
    nums = [7735,1962,8151,6879,4106,188,743,7444,7014,7705,5798,754,6360,3168,632,4371,2365,2503,2032,1484,9522,6926,4816,3008,8351,8907,2403,5562,4218,5897,2951,2496,8025,7563,5713,2792,2014,7877,259,8658,9336,1225,8736,5790,9010,2021,1768,187,989,8923,745,5284,3055,4762,7788,8612,1268,9662,8787,7761]

    
    # bad = 0
    # for i in range(len(nums)):
    #     # print(nums[i])
    #     for j in range(i+1, len(nums)):
            
    #         # print(nums[j])
    #         if j - i == nums[j] - nums[i]:
    #         #     print(nums[i])
    #         #     print(nums[j])
    #             bad += 1
            

    #             # print("--------")

    # print(bad)
    # print(len(nums)*(len(nums)-1)/2 - bad)

    
    bad = 0
    tmp = [n-i for i,n in enumerate(nums)]
    cnts = Counter(n-i for i,n in enumerate(nums))
    LEN = len(nums)
    print(sum(i*(LEN-i) for i in cnts.values())//2)