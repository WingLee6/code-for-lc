#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start

from typing import List
from sortedcontainers import SortedList

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sort_list = SortedList()
        for num in nums:
            if num not in sort_list:
                sort_list.add(num)
                if len(sort_list) > 3:
                    sort_list.pop(0)
        return sort_list[0] if len(sort_list) == 3 else sort_list[-1]

# @lc code=end

