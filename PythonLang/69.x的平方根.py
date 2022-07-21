# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 8:05 PM
# @Author  : lee
# @FileName: q69_x的平方根.py
# @Desc    :


"""
69_x的平方根

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while (num+1) * (num+1) <= x:
            num += 1

        return num


if __name__ == '__main__':
    param = 0

    solution = Solution()
    result = solution.mySqrt(x=param)
    print(result)

"""
示例 1：
输入：x = 4
输出：2

示例 2：
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

示例 2：
输入：x = 0
输出：0

"""
