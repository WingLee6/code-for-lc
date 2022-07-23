#
# @lc app=leetcode.cn id=2176 lang=python3
#
# [2176] 统计数组中相等且可以被整除的数对
#

# @lc code=start

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and ((i*j) % k == 0):
                    n += 1
        return n


# @lc code=end
