# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 
# @Author  : li
# @FileName: q4_寻找两个正序数组的中位数.py
# @Desc    : 寻找两个正序数组的中位数



"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 合并两个列表
        nums1[len(nums1):] = nums2
        # 新列表排序
        nums1.sort()
        # 中位数下标
        mid_int = math.floor((len(nums1) - 1) / 2)
        # print(nums1)
        # print(mid_int)
        # 判断中位数
        if len(nums1) % 2 == 0:
            return (nums1[mid_int]+nums1[mid_int+1])/2
        else:
            return nums1[mid_int]




if __name__ == '__main__':
    # 测试用例
    nums1_list = [1, 3]
    nums2_list = [2]

    result_float = Solution()
    print(result_float.findMedianSortedArrays(nums1_list, nums2_list))
    print('________________________________________')
    print(result_float.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))