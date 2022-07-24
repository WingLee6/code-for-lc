#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
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

# @lc code=end


"""
输入:[12, 3, 12, 12, 72]
输出:[1,3]
"""
