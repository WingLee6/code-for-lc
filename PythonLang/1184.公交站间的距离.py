#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        return min(sum(distance[min(start, destination):max(start, destination)]), sum(distance[max(start, destination):]+distance[:min(start, destination)]))
# @lc code=end

"""
input:[1,2,3,4]\n0\n1
output:1

input:[1,2,3,4]\n0\n2
output:3

input:[1,2,3,4]\n0\n3
output:4

input: [7,10,1,12,11,14,5,0]\n7\n2
ouutput: 17

"""