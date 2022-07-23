#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_num = 0
        for i in range(len(str(num))-k+1):
            if int(str(num)[i:i+k]) != 0 and num % int(str(num)[i:i+k]) == 0:
                k_num += 1

        return k_num

# @lc code=end


"""

输入: 430043\n2
输出: 2

输入: 2\n1
输出: 1
"""
