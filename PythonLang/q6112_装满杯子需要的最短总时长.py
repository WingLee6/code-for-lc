# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 8:20 AM
# @Author  : lee
# @FileName: q6112_装满杯子需要的最短总时长.py
# @Desc    :

"""
6112. 装满杯子需要的最短总时长

现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。

给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

"""
import math
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        算法思想：基于贪心，每次将最多的两类-1 或 唯一剩余的一类-1，直至结束
        :param amount:
        :return:
        """
        # 贪心
        num = 0
        amount.sort(reverse=True)
        while amount[0] != 0:
            print(amount)
            amount[0] -= 1
            if amount[1] != 0:
                amount[1] -= 1

            num += 1
            amount.sort(reverse=True)


        return num



if __name__ == '__main__':
    input = [2,5,3]
    solution = Solution()
    result = solution.fillCups(amount=input)
    print(result)


"""
示例 1：
输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。

示例 2：
输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。

示例 3：
输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。

示例 4：
输入：amount = [2,4,2]
输出：4

示例 5：
输入：amount = [0, 0, 0]
输出：0

示例 6：
输入：amount = [3, 9, 3]
输出：9

示例 7：
输入：amount = [2,5,3]
输出：5
"""