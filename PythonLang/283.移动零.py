#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from operator import length_hint
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        while 0 in nums[:length]:
            nums.remove(0)
            length -= 1
            nums.append(0)


# @lc code=end

