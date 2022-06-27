# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 
# @Author  : li
# @FileName: q13_罗马数字转整数.py
# @Desc    :


"""
13. 罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # 整理对应关系
        key_words = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]

        # 待返回数字
        num = 0
        # 字符串长度
        length = len(s)
        # 当字符串未遍历完
        while length > 0:
            # 当前字符代表数字>=下一字符代表数字： 表明没有逆序； 并且 如果是最后一个字符直接加上去
            if key_words.index(s[-length]) >= key_words.index(s[-length+1]) or length == 1:
                num += value[key_words.index(s[-length])]
            else:
                num -= value[key_words.index(s[-length])]
            length -= 1

        return num


if __name__ == '__main__':
    s = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(s=s)
    print(result)

"""
示例  1:
输入:  s = "III"
输出: 3

示例  2:
输入:  s = "IV"
输出: 4

示例  3:
输入:  s = "IX"
输出: 9

示例  4:
输入:  s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例  5:
输入:  s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

"""
