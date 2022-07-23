#
# @lc app=leetcode.cn id=2160 lang=python3
#
# [2160] 拆分数位后四位数字的最小和
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:

        return int(sorted(list(str(num)))[0])*10 + int(sorted(list(str(num)))[3]) + int(sorted(list(str(num)))[1])*10 + int(sorted(list(str(num)))[2])


# @lc code=end
