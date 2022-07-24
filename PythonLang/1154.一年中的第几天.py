#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            days[1] = 29
            
        return d + sum(days[:m-1])


# @lc code=end
