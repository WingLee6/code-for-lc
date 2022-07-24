#
# @lc app=leetcode.cn id=1545 lang=python3
#
# [1545] 找出第 N 个二进制字符串中的第 K 位
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        def findInvert(s):
            newString = ""
            for i in range(len(s)):
                # print("Input",s)
                if s[i] == "0":
                    newString += "1"
                    # print("Invert",s)
                else:
                    newString += "0"
            return newString
        
        def findReverse(s):
            return s[::-1]
        
        for i in range(n):
            invert = findInvert(s)
            reverse = findReverse(invert)
            s = s + "1" + reverse
            # print(s)
        
        return s[k-1]


# @lc code=end

