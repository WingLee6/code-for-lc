# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 7:23 AM
# @Author  : lee
# @FileName: q6164_数位和相等数对的最大和.py
# @Desc    :
from collections import defaultdict
from typing import List
from unittest import result

"""
6164. 数位和相等数对的最大和

给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。

请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def _maximumSum(self, nums: List[int]) -> int:
        """一般方法，leetcode会判超时

        :param nums:
        :return:
        """
        sum = [0] * len(nums)
        for i in range(len(nums)):
            for j in str(nums[i]):
                sum[i] += int(j)

        find_max = [-1]
        while sum:
            tmp = sum[0]
            if sum.count(tmp) >= 2:
                tmp_list = []
                while tmp in sum:
                    index = sum.index(tmp)
                    tmp_list.sort(reverse=False)
                    if len(tmp_list) <= 2 or nums[index] > tmp_list[0]:
                        tmp_list.append(nums[index])
                    sum.pop(index)
                    nums.pop(index)

                tmp_list.sort(reverse=True)
                find_max.append(tmp_list[0] + tmp_list[1])
            else:
                sum.remove(tmp)
                nums.pop(0)

        return max(find_max)

    def maximumSum(self, nums: List[int]) -> int:
        """
        来源网络

        defaultdict(param) 相当于给字典设置一个默认值
            默认值包括
            1. 默认key值
            2. 默认value值
                defaultdict(int)， 则默认value值为0
                defaultdict(str)， 则默认value值为''
                defaultdict(set)， 则默认value值为set()
                defaultdict(list)， 则默认value值为[]

                dic1 = defaultdict(int)
                dic2 = defaultdict(str)
                dic3 = defaultdict(set)
                dic4 = defaultdict(list)
                print(dic1["任何key"])
                print(dic2["任何key"])
                print(dic3["任何key"])
                print(dic4["任何key"])
                #0
                #
                #set()
                #[]

            解析 1：
            若
                dic = {}
                dic['A'].append(5)
                print(dic)
                # 因为字典没有key等于'A'，所以报错
            若改正上述错误，应为
                dic = {}
                dic.setdefault('A', [])
                dic['A'].append(5)
                print(dic)
                # 正常运行，第二行设置了默认key值
                # 但是每次都setdefault设置，很麻烦
                # 可用 defaultdict 函数简化代码
            使用 defaultict(param) 实现有默认值的定义字典：
                dic = defaultdict(list)
                dic['A'].append(5)
                print(dic)

        ord() 函数：返回对应的 ASCII 数值

        sort函数:sort函数没有返回值,会改变原元素的值
        sorted函数:sorted函数有返回值,不会改变原元素的值

        :param nums:
        :return:
        """

        cor = defaultdict(list)

        for num in nums:
            c = 0
            for i in str(num):
                c += ord(i) - ord('0')
            cor[c].append(num)

        ans = -1
        for c, l in cor.items():
            if len(l) >= 2:
                ans = max(ans, sum(sorted(l)[-2:]))
        return ans


if __name__ == '__main__':
    param = [4, 6, 10, 6]  # 12
    param = [229, 398, 269, 317, 420, 464, 491, 218, 439, 153, 482, 169, 411, 93, 147, 50, 347, 210, 251, 366, 401]
    p = Solution()
    result = p.maximumSum(nums=param)
    print(result)



"""
示例 1：
输入：nums = [18,43,36,13,7]
输出：54
解释：满足条件的数对 (i, j) 为：
- (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
- (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
所以可以获得的最大和是 54 。

示例 2：
输入：nums = [10,12,19,14]
输出：-1
解释：不存在满足条件的数对，返回 -1 。

示例 3：
输入：[4, 6, 10, 6]  
输出： 12

示例 4：
输入：[229, 398, 269, 317, 420, 464, 491, 218, 439, 153, 482, 169, 411, 93, 147, 50, 347, 210, 251, 366, 401]  
输出： 973
"""
