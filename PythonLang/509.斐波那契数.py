#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5**0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)

# @lc code=end

