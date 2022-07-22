#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_sale = 0
        input_day = len(prices)-1
    
        while input_day != 0:
            input_day = prices.index(min(prices[:input_day]))
            output_day = prices.index(max(prices[input_day:]))
            best_sale = prices[output_day]-prices[input_day] if prices[output_day]-prices[input_day]>best_sale else best_sale 
        
        return best_sale
# @lc code=end

"""
输入:[7,1,5,3,6,4]
输出: 5

输入: [7,6,4,3,1]
输出: 0

输入: [2,4,1]
输出: 2

输入: [1, 2, 3, 4]
输出: 3

输入: [1]
输出: 0
"""