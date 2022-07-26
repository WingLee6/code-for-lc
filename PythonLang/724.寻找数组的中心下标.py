#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i+1:])
           
            if sum_left == sum_right:
                return i
        
        return -1
# @lc code=end

