# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 8:40 AM
# @Author  : lee
# @FileName: q28_实现 strStr().py
# @Desc    :

"""
28. 实现 strStr()

实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。


"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)


if __name__ == '__main__':
    input = "hello"
    input2 = "bba"
    solution = Solution()
    result = solution.strStr(haystack=input, needle=input2)
    print(result)


"""
示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

"""
