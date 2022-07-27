#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        return sum(not Counter(w) - Counter(chars) and len(w) for w in words)


# @lc code=end
