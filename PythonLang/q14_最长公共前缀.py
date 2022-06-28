# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 
# @Author  : li
# @FileName: q14_最长公共前缀.py
# @Desc    :


"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 空列表，则直接返回空字符串
        if not strs:
            return ""
        # 直接对比：列表的最小和最大
        min_str, max_str = min(strs), max(strs)

        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str


if __name__ == '__main__':
    str_list = ["fraower","flaow","flaight"]
    # str_list = []
    solution = Solution()
    result = solution.longestCommonPrefix(strs=str_list)
    print(result)

"""
示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
。
"""
