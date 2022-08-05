#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_list = sorted(score, reverse=True)

        for i in range(len(sorted_list)):
            score[i] = str(sorted_list.index(score[i])+1)
            if score[i] == "1":
                score[i] = "Gold Medal"
            if score[i] == "2":
                score[i] = "Silver Medal"
            if score[i] == "3":
                score[i] = "Bronze Medal"

        return score


# @lc code=end
