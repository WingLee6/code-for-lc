# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 11:50 PM
# @Author  : lee
# @FileName: q53_最大子数组和.py
# @Desc    :

"""
53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        sumimum = min(nums)
        temp = 0
        for i in nums:
            if temp > 0:
                temp += i
            else:
                temp = i

            if temp > sumimum:
                sumimum = temp

        return sumimum


if __name__ == '__main__':
    input = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    result = solution.maxSubArray(nums=input)
    print(result)



"""
示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23

示例 4：
输入：nums = [-1]
输出：-1

"""