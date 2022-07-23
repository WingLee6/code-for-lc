#
# @lc app=leetcode.cn id=2315 lang=python3
#
# [2315] 统计星号
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        num = 0
        j = False
        for i in s:
            if i == '|' and not j:
                j = True
            elif i == '|' and j:
                j = False
            if i == '*' and not j:
                num += 1

        return num
        
# @lc code=end

"""
输入:"l|*e*et|c**o|*de|"
输出:2

输入:"iamprogrammer"
输出:0

输入:"yo|uar|e**|b|e***au|tifu|l"
输出:5
"""

