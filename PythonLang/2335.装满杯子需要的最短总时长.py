#
# @lc app=leetcode.cn id=2335 lang=python3
#
# [2335] 装满杯子需要的最短总时长
#

# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        算法思想:基于贪心，每次将最多的两类-1 或 唯一剩余的一类-1，直至结束
        :param amount:
        :return:
        """
        # 贪心
        num = 0
        amount.sort(reverse=True)
        while amount[0] != 0:
            # print(amount)
            amount[0] -= 1
            if amount[1] != 0:
                amount[1] -= 1

            num += 1
            amount.sort(reverse=True)


        return num
# @lc code=end



"""
示例 3:
输入:amount = [5,0,0]
输出:5
解释:每秒装满一杯冷水。

示例 4:
输入:amount = [2,4,2]
输出:4

示例 5:
输入:amount = [0, 0, 0]
输出:0

示例 6:
输入:amount = [3, 9, 3]
输出:9

示例 7:
输入:amount = [2,5,3]
输出:5
"""
