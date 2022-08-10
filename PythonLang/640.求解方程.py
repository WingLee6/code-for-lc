#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:

    def solveEquation(self, equation: str) -> str:
        def _counter(equation: str):
            num = 0
            x = 0
            if equation[0] not in ['+', '-']:
                equation = '+' + equation

            equation = equation + '!'

            start = 0
            for i, e in enumerate(equation):
                if i == 0:
                    continue

                if e in ['+', '-', '!']:
                    if equation[i-1] != 'x':
                        if equation[start] == '+':
                            num += int(float(equation[start+1:i]))
                        elif equation[start] == '-':
                            num -= int(float(equation[start+1:i]))

                    elif equation[i-1] == 'x':
                        if i-start == 2:
                            if equation[start] == '+':
                                x += 1
                            elif equation[start] == '-':
                                x -= 1
                        else:
                            if equation[start] == '+':
                                x += int(float(equation[start+1:i-1]))
                            elif equation[start] == '-':
                                x -= int(float(equation[start+1:i-1]))

                    start = i

            return [num, x]

        l = _counter(equation[:equation.find('=')])
        left_num = l[0]
        left_x = l[1]
        l = _counter(equation[equation.find('=')+1:])
        right_num = l[0]
        right_x = l[1]

        if left_x != right_x:
            return "x=" + str(int((right_num-left_num) / (left_x-right_x)))

        if left_x == right_x and right_num-left_num != 0:
            return "No solution"

        if left_x == right_x:
            return "Infinite solutions"

# @lc code=end


equation = "x+5-3+x=6+x-2"
s = Solution()
print(s.solveEquation(equation))
