#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)

        return [nums.most_common(1)[0][0], list((Counter([i for i in range(1, len(nums)+2)]) - nums).keys())[0]]


# @lc code=end
s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
