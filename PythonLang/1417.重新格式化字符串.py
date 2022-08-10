#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
from curses.ascii import isalpha
import re


class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chars = []
        for i in s:
            if i.isdigit():
                nums.append(i)
            if i.isalpha():
                chars.append(i)

        if abs(len(nums)-len(chars)) > 1:
            return ""
        elif len(nums) == 0 or len(chars) == 0:
            return "".join(nums) if len(chars) == 0 else "".join(chars)

        elif len(nums) < len(chars):
            for i in range(len(nums)):
                nums.insert(i*2, chars[i])

            nums.append(chars[i+1])
            return ''.join(nums)
        elif len(nums) > len(chars):
            for i in range(len(chars)):
                chars.insert(i*2, nums[i])

            chars.append(nums[i+1])
            return ''.join(chars)
        else:
            for i in range(len(nums)):
                nums.insert(i*2, chars[i])
            return ''.join(nums)


# @lc code=end

s = Solution()
print(s.reformat("j"))
print("0000000")
