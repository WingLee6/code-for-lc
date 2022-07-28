#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        return len(set(candyType)) if len(set(candyType)) < len(candyType)/2 else len(candyType)//2

# @lc code=end
