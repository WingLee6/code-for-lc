#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        per_candies = [0] * num_people
        i = 0
        while candies >= 0:           
            per_candies[i%num_people] += min(i+1, candies)
            candies -= i+1
            i += 1
        
        return per_candies
            

# @lc code=end

