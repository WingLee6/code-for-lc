#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
from ast import Num
import re

from pyparsing import nums


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [0] * len(ratings)
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right = candy_sum = 0
        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings)  - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            candy_sum += max(left[i], right)
        
        return candy_sum
# @lc code=end


"""
input:[1, 0, 5, 8, 2, 4, 3]
output:12
解析: 分别要给的糖果
1, 1+1, 2, 3, 1, 2, 1

input: [2, 8, 7, 2, 1, 0, 1]
output: 18


"""
