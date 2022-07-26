#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index_ch = word.find(ch) + 1
        return word[:index_ch][::-1] + word[index_ch:]
        
# @lc code=end

