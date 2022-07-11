# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 11:14 AM
# @Author  : lee
# @FileName: q6115_统计理想数组的数目.py
# @Desc    :

'''
q6115_统计理想数组的数目

给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。

对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：

每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。
返回长度为 n 的 不同 理想数组的数目。

由于答案可能很大，返回对 109 + 7 取余的结果。

'''
from collections import Counter
from functools import lru_cache
from math import floor

MOD = int(1e9 + 7)

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        res = 0
        for end in range(1, maxValue + 1):
            cur = 1
            counter = getPrimeFactors(end)
            for _, k in counter.items():
                # !n-1个物品放到k+1个槽(1,p,p^2,...p^k)里 选k个隔板 隔板可重复选
                # !itertools.combinations_with_replacement
                cur *= CWithReplacement(n - 1, k + 1)
                cur %= MOD
            res += cur
            res %= MOD
        return res


@lru_cache(None)
def getPrimeFactors(n: int,) -> Counter[int]:
    """返回 n 的质因子分解"""
    res = Counter()
    upper = floor(n**0.5) + 1
    for i in range(2, upper):
        while n % i == 0:
            res[i] += 1
            n //= i

    if n > 1:
        res[n] += 1
    return res


@lru_cache(None)
def fac(n: int) -> int:
    """n的阶乘"""
    if n == 0:
        return 1
    return n * fac(n - 1) % MOD


@lru_cache(None)
def ifac(n: int) -> int:
    """n的阶乘的逆元"""
    return pow(fac(n), MOD - 2, MOD)


def C(n: int, k: int) -> int:
    if n < 0 or k < 0 or n < k:
        return 0
    return ((fac(n) * ifac(k)) % MOD * ifac(n - k)) % MOD


def CWithReplacement(n: int, k: int) -> int:
    """
    可以选取重复元素的组合数
    n个物品放入k个槽(槽可空)的方案数
    """
    return C(n + k - 1, k - 1)


if __name__ == '__main__':
    solution = Solution()
    result = solution.idealArrays(n=2, maxValue=5)
    print(result)

"""
示例 1：

输入：n = 3, maxValue = 5
输出：10
解释：存在以下理想数组：
- 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
- 以 2 开头的数组（2 个）：[2,2]、[2,4]
- 以 3 开头的数组（1 个）：[3,3]
- 以 4 开头的数组（1 个）：[4,4]
- 以 5 开头的数组（1 个）：[5,5]
共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。
示例 2：

输入：n = 5, maxValue = 3
输出：11
解释：存在以下理想数组：
- 以 1 开头的数组（9 个）：
   - 不含其他不同值（1 个）：[1,1,1,1,1] 
   - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- 以 2 开头的数组（1 个）：[2,2,2,2,2]
- 以 3 开头的数组（1 个）：[3,3,3,3,3]
共计 9 + 1 + 1 = 11 个不同理想数组。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-the-number-of-ideal-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""