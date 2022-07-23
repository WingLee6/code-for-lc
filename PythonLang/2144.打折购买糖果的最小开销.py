#
# @lc app=leetcode.cn id=2144 lang=python3
#
# [2144] 打折购买糖果的最小开销
#

# @lc code=start
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        tmp_cost_price = 0
        gift = 0
        while cost:
            if gift != 2:
                tmp_cost_price += max(cost)
                gift += 1
            elif gift == 2:
                gift = 0

            cost.pop(cost.index(max(cost)))

        return tmp_cost_price
# @lc code=end
