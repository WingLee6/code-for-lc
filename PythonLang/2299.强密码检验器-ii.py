#
# @lc app=leetcode.cn id=2299 lang=python3
#
# [2299] 强密码检验器 II
#

# @lc code=start
from curses.ascii import islower
from enum import Flag
from re import S


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lower = False
        has_upper = False
        has_digit = False
        has_special_char = False
        spcl_char = "!@#$%^&*()-+"
        for i in password:
            if i.islower():
                has_lower = True
            if i.isupper():
                has_upper = True
            if i.isdigit():
                has_digit = True
            if i in spcl_char:
                has_special_char = True
            if has_lower and has_upper and has_digit and has_special_char:
                continue
        for i in range(1, len(password)):
            if(password[i-1] == password[i]):
                return False

        if (has_lower and has_upper and has_digit and has_special_char):
            return True
        else:
            return False

# @lc code=end
