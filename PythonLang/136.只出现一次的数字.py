#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 法1: 效果略差
        # nums_set = set(nums)
        # for i in nums_set:
        #     if nums.count(i) == 1:
        #         return i
        
        # 法2:来源网络
        ret=0
        for num in nums:
            # ^ 按位异或运算符 同0异1
            ret=ret^num
            
        return ret


        
# @lc code=end

