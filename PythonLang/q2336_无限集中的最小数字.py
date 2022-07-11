# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 10:03 AM
# @Author  : lee
# @FileName: q2336_无限集中的最小数字.py
# @Desc    :

"""
2336. 无限集中的最小数字

现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。

实现 SmallestInfiniteSet 类：

SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
int popSmallest() 移除 并返回该无限集中的最小整数。
void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/smallest-number-in-infinite-set
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List
from sortedcontainers import SortedSet as SS

class SmallestInfiniteSet:

    def __init__(self):
        self.SmallestInfiniteSet = []
        for i in range(1, 2000):
            self.SmallestInfiniteSet.append(i)


    def popSmallest(self) -> int:
        min_num = min(self.SmallestInfiniteSet)
        self.SmallestInfiniteSet.remove(min(self.SmallestInfiniteSet))
        return min_num


    def addBack(self, num: int) -> None:
        if num not in self.SmallestInfiniteSet:
            self.SmallestInfiniteSet.append(num)

        return None

    def operate(self, op_list: List[str], param_list: List[List[int]]) -> list:

        result_list = []
        for (op, param) in zip(op_list, param_list):
            if op == "addBack":
                self.addBack(param[0])
                result_list.append(None)
            elif op == "popSmallest":
                result_list.append(self.popSmallest())
            else:
                result_list.append(None)

        return result_list



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


if __name__ == '__main__':
    input = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
    input2 = [[], [2], [], [], [], [1], [], [], []]

    input = ["SmallestInfiniteSet", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "addBack",
     "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest"]
    input2 = [[], [], [], [], [771], [], [330], [], [], [631], [], []]

    input = ["SmallestInfiniteSet", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
     "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest"]
    input2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
     [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    solution = SmallestInfiniteSet()
    result = SmallestInfiniteSet().operate(op_list=input, param_list=input2)
    print(result)


"""
实例1：
输入
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
输出
[null, null, 1, 2, 3, null, 1, 4, 5]

解释
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。
smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，
                                   // 且 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。



实例2：
输入：
["SmallestInfiniteSet","popSmallest","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","popSmallest","popSmallest"]
[[],[],[],[],[771],[],[330],[],[],[631],[],[]]
输出：
[null,1,2,3,null,4,null,5,6,null,7,8]

实例3：
["SmallestInfiniteSet","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest","popSmallest"]
[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

[1, 2
"""