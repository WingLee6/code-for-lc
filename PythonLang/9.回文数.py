# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 
# @Author  : li
# @FileName: q9_回文数.py
# @Desc    :



"""
9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


https://leetcode.cn/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数一定为非回文数，直接返回False
        if x < 0:
            return False

        # 最高位下标
        high = len(str(x))-1
        low = 0
        # 字符长度为奇数，则mid=中间数下标；字符长度为偶数，则mid=中间数下标-1，
        mid = (len(str(x))-1)//2

        # 目前下标为high和low两个数满足回文 and 未循环完整
        while str(x)[high] == str(x)[low] and high > mid:
            high -= 1
            low += 1

        # 返回结果
        return high == mid






if __name__ == '__main__':
    num = 123456787654321
    solution = Solution()
    result = solution.isPalindrome(x=num)
    print(result)

"""
示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
