#
# @lc app=leetcode.cn id=6129 lang=python3
#
# [6129] 全 0 子数组的数目
#

# @lc code=start

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # 超时！
        # zero_num = 0

        # i = 0
        # while i <= len(nums)-1:
        #     l_zero = next((i for i, x in enumerate(nums[i:]) if x), 0) if len(nums[i:]) != nums[i:].count(0) else nums[i:].count(0)
        #     i += l_zero+1
        #     zero_num += int(l_zero*(1+l_zero)/2)

        # return zero_num


        # 来源网络
        zero_num = 0
        c = 0
        
        for i in nums:
            if i == 0:
                c += 1
                zero_num += c   # 在循环的同时累加，妙！
            else:
                c = 0
        return zero_num


# @lc code=end
