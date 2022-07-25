#
# @lc app=leetcode.cn id=2332 lang=python3
#
# [2332] 坐上公交的最晚时间
#

# @lc code=start
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:        
        buses.sort()
        passengers.sort()
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                c -= 1
                j += 1
        j -= 1
        ans = buses[-1] if c else passengers[j]  # 在发车时到达公交站 or 上一个上车的乘客
        while j >= 0 and passengers[j] == ans:  # 往前找没人到达的时刻
            ans -= 1
            j -= 1
        return ans
# @lc code=end

