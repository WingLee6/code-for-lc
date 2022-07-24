#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start

class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        i = 0
        while i < len(s):
            tmp_length = 1
            while i+tmp_length < len(s) and s[i] == s[i+tmp_length]:
                tmp_length += 1

            max_length = tmp_length if tmp_length > max_length else max_length
            i += tmp_length

        return max_length
# @lc code=end
