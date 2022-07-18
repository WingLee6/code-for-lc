# -*- coding: utf-8 -*-
# @Time    : 2022/7/17 9:15 PM
# @Author  : lee
# @FileName: q6120_数组能形成多少数对.py
# @Desc    :
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result = [0, 0]

        while nums:
            tmp = nums[0]
            if nums.count(tmp) >= 2:
                nums.remove(tmp)
                nums.remove(tmp)
                result[0] += 1
            else:
                nums.remove(tmp)
                result[1] += 1

        return result




if __name__ == '__main__':
    param = [12, 3, 12, 12, 72]
    s = Solution()
    result = s.numberOfPairs(nums=param)
    print(result)



"""
输入：nums = [1,3,2,1,3,2,2]
输出：[3,1]
解释：
nums[0] 和 nums[3] 形成一个数对，并从 nums 中移除，nums = [3,2,3,2,2] 。
nums[0] 和 nums[2] 形成一个数对，并从 nums 中移除，nums = [2,2,2] 。
nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [2] 。
无法形成更多数对。总共形成 3 个数对，nums 中剩下 1 个数字。
示例 2：

输入：nums = [1,1]
输出：[1,0]
解释：nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [] 。
无法形成更多数对。总共形成 1 个数对，nums 中剩下 0 个数字。
示例 3：

输入：nums = [0]
输出：[0,1]
解释：无法形成数对，nums 中剩下 1 个数字。



"""

