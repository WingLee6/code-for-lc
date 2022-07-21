#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        layer = []
        for i in range(numRows):
            layer.append([1]*(i+1))
            for j in range(i-1):
                layer[i][j+1] = layer[i-1][j] + layer[i-1][j+1]

        return layer
# @lc code=end


"""
input 5
output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

input 1
output [[1]]

input 5
output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
