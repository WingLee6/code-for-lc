#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
from collections import Counter
from itertools import count
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_dict = Counter(list(set(nums1))) - Counter(list(set(nums2))) if Counter(list(set(
            nums1))) - Counter(list(set(nums2))) else Counter(list(set(nums2))) - Counter(list(set(nums1)))

        return list(set([i for i in nums1 if i not in counter_dict.keys()]))
# @lc code=end
