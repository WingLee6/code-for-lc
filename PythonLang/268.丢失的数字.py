#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == max(nums)+1:
            return len(nums)

        for i in range(max(nums)):
            if i not in nums:
                return i


# @lc code=end
