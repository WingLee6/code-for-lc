#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        tmp_lucky_numbers = []
        lucky_numbers = []
        for i, row in enumerate(matrix):
            tmp_lucky_numbers.append(min(row))

        for i in range(len(matrix[0])):
            line_max = max([matrix[j][i] for j in range(len(matrix))])
            if line_max in tmp_lucky_numbers:
                lucky_numbers.append(line_max)

        return lucky_numbers

# @lc code=end
