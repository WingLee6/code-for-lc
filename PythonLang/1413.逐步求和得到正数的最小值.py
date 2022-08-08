#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 0
        tmp_sum = 0
        for i in nums:
            tmp_sum += i
            startValue = tmp_sum if tmp_sum < 1 and tmp_sum < startValue else startValue

        return 1-startValue

# @lc code=end
