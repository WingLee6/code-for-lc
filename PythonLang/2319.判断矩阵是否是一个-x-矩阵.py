#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

# @lc code=start
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, cow in enumerate(grid):

            i = len(cow)-1-i if i > len(cow)-1-i else i
            if cow[i] == 0 or cow[len(cow)-1-i] == 0 \
                    or cow[:i].count(0) != i\
                    or (len(cow)-2-2*i != -1 and cow[i+1:len(cow)-1-i].count(0) != len(cow)-2-2*i)\
                    or cow[len(cow)-i:].count(0) != i:

                return False

        return True

# @lc code=end
