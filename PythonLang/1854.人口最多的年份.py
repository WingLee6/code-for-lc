#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#

# @lc code=start
from collections import defaultdict
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic = defaultdict(int)
        for age in logs:
            for y in range(age[0], age[1]):
                dic[y] += 1
        
        return [key for key, value in SortedDict(dic).items() if value == max(dic.values())][0]

# @lc code=end


param = [[1950, 1961], [1960, 1971], [1970, 1981]]
s = Solution()
print(s.maximumPopulation(param))


