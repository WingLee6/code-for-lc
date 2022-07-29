#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for chr in t:
            if i == len(s):
                continue
            if s[i] == chr:
                i += 1
        if i == len(s):
            return True
        else:
            return False


# @lc code=end

