#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 法1: 
        # visited = []
        # for i in nums:
        #     if i not in visited and nums.count(i) > len(nums)//2:
        #         return i

        #     visited.append(i) 


        # 法2: collections法
        counts = collections.Counter(nums)
        print(counts.keys())
        return max(counts.keys(), key=counts.get)


               
# @lc code=end

