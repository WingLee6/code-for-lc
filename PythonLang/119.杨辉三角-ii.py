#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        layer = []
        for i in range(rowIndex+1):
            layer.append([1]*(i+1))
            for j in range(i-1):
                layer[i][j+1] = layer[i-1][j] + layer[i-1][j+1]
        return layer[rowIndex]        
# @lc code=end

