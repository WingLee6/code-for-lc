#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start
from this import d


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([word.lower() if len(word) < 3 else word.title() for word in title.split()])


# @lc code=end

