#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic = defaultdict(int)
        for age in logs:
            for y in range(age[0], age[1]):
                dic[y] += 1

        return int(str(sorted(dic.items()))[str(sorted(dic.items())).find(", " + str(max(dic.values())) + ")")-4: str(sorted(dic.items())).find(", " + str(max(dic.values())) + ")")])

# @lc code=end


s = Solution()
print(s.maximumPopulation([[2000,2001]]))
