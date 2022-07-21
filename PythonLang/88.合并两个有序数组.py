# -*- coding: utf-8 -*-
# @Time    : 2022/7/14 12:43 PM
# @Author  : lee
# @FileName: q88_合并两个有序数组.py
# @Desc    :


"""
88. 合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del_zero = len(nums1) - m
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        for j in range(del_zero):
            nums1.remove(0)
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    solution.merge(nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3)

"""
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

示例 4：
输入：
nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3
输出：
[-1,0,0,1,2,2,3,3,3]
"""
