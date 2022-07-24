#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
from scipy.spatial import ConvexHull
import numpy as np


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # 算三角形面积
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2


        # 找到凸包
        # https://baike.baidu.com/item/%E5%87%B8%E5%8C%85/179150?fr=aladdin
        # https://blog.csdn.net/weixin_35757704/article/details/122707064
        points_np = np.array(points)
        hull = ConvexHull(points_np)
        # print(points_np[hull.vertices])
        convexHull = points_np[hull.vertices]


        # 根据凸包算面积
        ans, n = 0, len(convexHull)
        for i, p in enumerate(convexHull):
            k = i + 2
            for j in range(i + 1, n - 1):
                q = convexHull[j]
                while k + 1 < n:
                    curArea = triangleArea(p[0], p[1], q[0], q[1], convexHull[k][0], convexHull[k][1])
                    nextArea = triangleArea(p[0], p[1], q[0], q[1], convexHull[k + 1][0], convexHull[k + 1][1])
                    if curArea >= nextArea:
                        break
                    k += 1
                ans = max(ans, triangleArea(p[0], p[1], q[0], q[1], convexHull[k][0], convexHull[k][1]))
        return ans

    
# @lc code=end


"""


input: [[4,6],[6,5],[3,1]]
output: 5.5

"""
