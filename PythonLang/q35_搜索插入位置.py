# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 8:07 AM
# @Author  : lee
# @FileName: q35_搜索插入位置.py
# @Desc    :


"""
35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 是否存在于数组中
        if target in nums:
            return nums.index(target)
        else:
            # 不存在于数组中
            # 找到合适的插入位置
            for i in nums:
                if i > target:
                    return nums.index(i)
            # 需要插入到数组末尾
            return len(nums)



if __name__ == '__main__':
    input = [1,3,5,6]
    solution = Solution()
    result = solution.searchInsert(nums=input, target=2)
    print(result)


"""
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

"""
