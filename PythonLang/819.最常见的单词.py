#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict = {}
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        for word in paragraph:            
            if word not in banned:
                if word in dict:
                    dict[word]+=1
                else:
                    dict[word]=1

        return max(dict, key=dict.get)



# @lc code=end

