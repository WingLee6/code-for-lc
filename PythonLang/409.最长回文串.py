#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dic = Counter(s)
        length = 0
        add_one = 0
        for key in count_dic.keys():
            length += count_dic[key] // 2
            count_dic[key] = count_dic[key] % 2
            if count_dic[key] % 2 == 1:
                add_one = 1

        return length*2 + add_one


# @lc code=end
