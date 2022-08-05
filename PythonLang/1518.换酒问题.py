#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunks = numBottles
        tmp_bottles = numBottles
        while tmp_bottles >= tmp_bottles:
            drunks += tmp_bottles//numExchange
            tmp_bottles = tmp_bottles//numExchange + tmp_bottles%numExchange
            
            if tmp_bottles < numExchange:
                break

        return drunks 
# @lc code=end

