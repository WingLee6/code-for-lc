# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 2:36 PM
# @Author  : lee
# @FileName: q67_二进制求和.py
# @Desc    :


"""
67. 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d = False       # 进位标志
        result_reverse = ""

        add_0 = "0"*abs(len(a)-len(b))
        if len(a) > len(b):
            b = add_0 + b
        else:
            a = add_0 + a
        length = len(a) - 1

        for i in range(len(a)):

            if d:
                sum = int(a[length]) + int(b[length]) + 1
            else:
                sum = int(a[length]) + int(b[length])

            if sum > 1:
                d = True
                sum -= 2
            else:
                d = False
            result_reverse += str(sum)
            length -= 1

        if d:
            result_reverse += "1"

        return result_reverse[::-1]


if __name__ == '__main__':
    param = "1010"
    param2 = "1011"

    solution = Solution()
    result = solution.addBinary(a=param, b=param2)
    print(result)

"""
示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

示例3:
输入: a = "1111", b = "1111"
输出: "11110"

示例3:
输入:
"1010"
"1011"
输出: "10101"

"""
