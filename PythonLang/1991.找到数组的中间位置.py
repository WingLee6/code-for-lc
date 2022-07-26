#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i+1:])

            if sum_left == sum_right:
                return i

        return -1


# @lc code=end


"""

input: [-1,2]
output: -1

input: [0,0,0,0]
output: 0

input:[3,-4,1,-4]
output:3
"""
