#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#
#  34
# @lc code=start
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for sentence in sentences:
            max_word = sentence.count(" ") if sentence.count(" ") > max_word else max_word

        return max_word+1

# @lc code=end


"""
["please wait", "continue to fight", "continue to win"]
3

"""
