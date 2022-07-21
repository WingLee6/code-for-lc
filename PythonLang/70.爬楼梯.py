# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 8:24 PM
# @Author  : lee
# @FileName: q70_爬楼梯.py
# @Desc    :

"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 爬到楼顶方法个数
from functools import lru_cache


class Solution:
    @lru_cache(None)        # 带有装饰器@lru_cache可以利用缓存减少迭代调用时间。不加次方法会超时
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    param = 38

    solution = Solution()
    result = solution.climbStairs(n=param)
    print(result)

"""
示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

"""
