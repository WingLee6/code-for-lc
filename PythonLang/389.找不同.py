#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(s)):
            if sorted(s)[i] != sorted(t)[i]:
                return sorted(t)[i]

        return sorted(t)[-1]


# @lc code=end


"""
input:" "ae" \n "aea" "
output:"a"


"""