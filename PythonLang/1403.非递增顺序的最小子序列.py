#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
from operator import le
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        tmp_nums = []
        while sum(tmp_nums) <= sum(nums):
            tmp_nums.append(max(nums))
            nums.remove(max(nums))

        return tmp_nums




# @lc code=end

