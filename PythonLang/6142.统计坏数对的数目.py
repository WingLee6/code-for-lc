#
# @lc app=leetcode.cn id=6142 lang=python3
#
# [6142] 统计坏数对的数目
#

# @lc code=start
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for idx, num in enumerate(nums):
            d[num-idx] += 1
        ans = 0
        for i in d.values():
            ans += i * (i - 1) // 2
        return len(nums) * (len(nums) - 1) // 2 - ans


# @lc code=end

