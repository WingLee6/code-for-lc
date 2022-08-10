#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#

# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:

        return [i for i in range(-n//2+1, n//2+1)] if n % 2 == 1 else [i for i in range(-n//2, n//2+1) if i != 0]
# @lc code=end


s = Solution()
print(s.sumZero(4))
