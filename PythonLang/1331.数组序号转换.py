#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 法1： 超时 排序+数组
        # sorted_list = sorted(list(set(arr)))
        # return [sorted_list.index(i)+1 for i in arr]

        # 法2： 排序+哈希表
        sorted_dict = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [sorted_dict[i] for i in arr]

# @lc code=end
