#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_nums = -1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_nums = nums[j] - nums[i] if nums[j] - \
                        nums[i] > max_nums else max_nums

        return max_nums


# @lc code=end

s = Solution()
s.maximumDifference([7, 1, 5, 4])
