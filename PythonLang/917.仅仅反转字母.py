#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            while left < len(s) and not s[left].isalpha():
                left += 1
            while right >= 0 and not s[right].isalpha():
                right -= 1

            if left < right:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp

            left += 1
            right -= 1
        return "".join(s)
# @lc code=end
