#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
from audioop import avg
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        tmp = sum(nums[:k])
        sum_num = tmp
        for i in range(1, len(nums)-k+1):
            tmp = tmp + nums[i+k-1] - nums[i-1]
            sum_num = tmp if tmp > sum_num else sum_num

        return sum_num / k


# @lc code=end

s = Solution()
print(s.findMaxAverage(nums=[0, 4, 0, 3, 2], k=1))
