#
# @lc app=leetcode.cn id=2338 lang=python3
#
# [2338] 统计理想数组的数目
#

from collections import Counter
from functools import lru_cache
from math import floor


# @lc code=start

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
# @lc code=end

