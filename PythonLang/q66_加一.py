# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 7:12 AM
# @Author  : lee
# @FileName: q66_加一.py
# @Desc    :
from typing import List

"""
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 列表 ----> int整数+1 ----> 列表
        # 转int整数
        length = len(digits)
        num = 1
        for i in digits:
            num += i * 10 ** (length-1)
            length -= 1

        # int整数 转 列表
        num_str_list = list(str(num))
        num_list = [int(x) for x in num_str_list]

        return num_list






if __name__ == '__main__':
    input = [1, 9, 9]
    solution = Solution()
    result = solution.plusOne(digits=input)
    print(result)

"""
示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
