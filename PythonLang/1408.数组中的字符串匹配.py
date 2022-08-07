#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # 一般方法
        # tmp_list = []
        # for i, word in enumerate(words):
        #     for w in words[i+1:]:
        #         if w in tmp_list or word in tmp_list:
        #             continue

        #         if w in word or word in w:
        #             tmp_list.append(w if len(w) < len(word) else word)
                    
        # return list(set(tmp_list))

        # 法2:
        # 来源网络
        words_str = str(words)
        return [w for w in words if words_str.count(w)>1]
# @lc code=end

