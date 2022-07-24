#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from re import T


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums, reverse=False) or nums == sorted(nums, reverse=True)
# @lc code=end
