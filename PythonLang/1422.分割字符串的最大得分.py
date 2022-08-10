#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        # 法1:
        max_score = 0
        left_score = 0
        right_score = s.count("1")

        for i in s[:len(s)-1]:
            if i == '0':
                left_score += 1
            else:
                right_score -= 1

            tmp = left_score + right_score       
            max_score = tmp if tmp > max_score else max_score
        return max_score

        # 法2:
        # max_score = 0
        # for i in range(1, len(s)):
        #     tmp = s[:i].count("0") + s[i:].count("1")
        #     max_score = tmp if tmp > max_score else max_score

        # return max_score

# @lc code=end


s = Solution()
print(s.maxScore("00"))
