#
# @lc app=leetcode.cn id=761 lang=python3
#
# [761] 特殊的二进制序列
#

# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        cnt = left = 0
        subs = list()

        for i, ch in enumerate(s):
            if ch == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left+1:i]) + "0")
                    left = i + 1
                    print(subs)
        
        subs.sort(reverse=True)
        return "".join(subs)
        

# @lc code=end

s = Solution()
result = s.makeLargestSpecial(s="11011000")
print(result)
