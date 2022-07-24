#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 法1:超时
        # for i in nums:
        #     if nums.count(i) >= 2:
        #         return True

        # return False

        # 法2:
        nums.sort()
        for i in range(len(nums[:len(nums)-1])):
            if nums[i] == nums[i+1]:
                return True
        return False
# @lc code=end
