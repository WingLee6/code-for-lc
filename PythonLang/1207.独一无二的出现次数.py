#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start

from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        count = []
        
        for i in dic:
            if dic[i] in count:
                return False
            count.append(dic[i])

        return True


# @lc code=end

